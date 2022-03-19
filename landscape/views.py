from django.shortcuts import redirect, render
from django.conf import settings
from django.http import JsonResponse
from django.apps import apps as django_apps
from landscape.models import Landscape, Like, Photo, Review
from authentication.models import User
from landscape.forms import LikeForm, ReviewForm
from landscape.models import Landscape, Photo, Review
from django.contrib.auth.decorators import login_required


def index(request):

    context_dict = {}
    context_dict['activities'] = django_apps.get_app_config('landscape').activities
    context_dict['accessibilities'] = django_apps.get_app_config(
        'landscape').accessibilities
    if request.method == 'GET':
        if request.GET.get('q'):
            context_dict['q'] = request.GET.get('q')
        return render(request, 'landscape/index.html', context=context_dict)


def show_landscape(request, landscape_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}
    try:
        landscape = Landscape.objects.get(slug=landscape_name_slug)
        reviews = Review.objects.filter(
            landscape_id=landscape.id).order_by('-visit_date')[:5]
        photos = Photo.objects.filter(landscape_id = landscape.id)
        
        for r in reviews:
            r.rating = roundRating(r.rating)
        context_dict['reviews'] = reviews
        context_dict['landscape'] = landscape
        context_dict['photos'] = photos
        context_dict['url'] = Photo.objects.first().image.url
        return render(request, 'landscape/landscape.html', context=context_dict)
    except Landscape.DoesNotExist:
        return redirect('landscape:index')

@login_required()
def add_review(request, landscape_name_slug):
    try:
        landscape = Landscape.objects.get(slug=landscape_name_slug)
    except Landscape.DoesNotExist:
        landscape = None

    if landscape is None:
        return redirect('/landscape/')

    form = ReviewForm()
    error_message = None

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        images = request.FILES.getlist('images')

        if form.is_valid():
            review = form.save(commit=False)
            review.landscape_id = landscape
            review.user_id = request.user
            review.save()

            for image in images:
                Photo.objects.create(review_id =review, image = image, landscape_id = landscape)
            return redirect('landscape:index')
        print(form.errors)
        error_message = form.errors

    context_dict = {}
    context_dict['form'] = form
    context_dict['landscape'] = landscape
    context_dict['activities'] = django_apps.get_app_config('landscape').activities
    context_dict['accessibilities'] = django_apps.get_app_config(
        'landscape').accessibilities
    context_dict['error_message'] = error_message
    return render(request, 'landscape/add_review.html', context=context_dict)


def search(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')
        location = {k: float(request.GET.get(k))
                    for k in ['lat', 'lon']} if request.GET.get('lat') else None
        # filters
        activities = request.GET.get('activities').split(',') if request.GET.get(
            'activities') and len(request.GET.get('activities').split(',')) > 0 else []
        accessibilities = request.GET.get('accessibilities').split(',') if request.GET.get(
            'accessibilities') and len(request.GET.get('accessibilities').split(',')) > 0 else []
        result = es_search(query, location = location, activities = activities, accessibilities = accessibilities)
        response = JsonResponse({"data": result, 'is_success': True})
        return response


def es_search(query = '', **filters):
        # query
        es_query = {
            'bool': {
                'must': [
                    {
                        'term': {
                            'is_active': True,
                        }
                }],
            }
        }
        if query:
            es_query['bool']['must'].append({
                'multi_match': {
                    'fields': ['*'],
                    'query': query,
                    'fuzziness': 'AUTO'
                }
            })

        # location
        if 'location' in filters and filters['location']:
            es_query['bool']['must'].append({
                'geo_distance': {
                    "distance": django_apps.get_app_config('landscape').GEO_DISTANCE,
                    "location": filters['location'],
                }
            })
        

        additional_filters = len(filters['activities']) > 0 or len(filters['accessibilities']) > 0
        es_query['bool']['should'] = [] if additional_filters else None
        es_query['bool']['minimum_should_match'] = 1 if additional_filters else None

        # add the filter to the query if exists
        if len(filters['activities']) > 0:
            es_query['bool']['should'].append({
                'terms': {
                    'activities': filters['activities'],
                }})

        if len(filters['accessibilities']) > 0:
            es_query['bool']['should'].append({
                'terms': {
                    'accessibilities': filters['accessibilities'],
                }})
        es = django_apps.get_app_config('landscape').es
        ## sorting
        SORTING = [
            {'review.average_rating': {'order': 'desc'}},
            {'review.count': {'order': 'desc'}}
        ]
        result = es.search(index=settings.ES_INDEX,
                           query=es_query, sort=SORTING)
        result = [data['_source'] for data in result.body['hits']['hits']]
        return result
       


def roundRating(rating):
    number = int(rating*100/5)
    hundreds = (number % 1000) // 100
    tens = (number % 100) // 10
    percentage = "" if hundreds == 0 else "1"
    return percentage

@login_required()
def add_like(request, landscape_name_slug):
    try:
        landscape = Landscape.objects.get(slug=landscape_name_slug)
    except Landscape.DoesNotExist:
        landscape = None

    if landscape is None:
        return redirect('/landscape/')

    if request.method == 'POST':
        form = LikeForm(request.POST)
        user = User.objects.first()
        liked = Like.objects.filter(user_id=user, landscape=landscape).exists()

        if liked==False:
            like = form.save(commit=False)
            like.landscape_id = landscape
            # TODO: replace this for the logged user
            like.user_id = user
            like.save()

            return redirect('/landscape/')

    context_dict = {}
    context_dict['form'] = form
    context_dict['landscape'] = landscape
    return render(request, 'landscape/landscape.html', context=context_dict)
