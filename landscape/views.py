from django.shortcuts import redirect, render
from django.conf import settings
from django.http import Http404, JsonResponse
from django.apps import apps as django_apps
from django.views.decorators.csrf import csrf_exempt
from landscape.models import Landscape, Photo, Review, saved_landscapes
import json
from landscape.forms import ReviewForm
from landscape.models import Landscape, Photo, Review
from django.contrib.auth.decorators import login_required
from utils import utils


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
        photos = Photo.objects.filter(landscape_id=landscape.id)

        #for r in reviews:
        #    r.rating = utils.roundRating(r.rating)
        liked = False
        try:
            liked = True if saved_landscapes.objects.get(landscape_id=landscape, user_id=request.user) else False
        except:
            liked = False
        context_dict['reviews'] = reviews
        context_dict['landscape'] = landscape
        context_dict['photos'] = photos
        context_dict['liked'] = liked
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
            review.rating=float(request.POST['rating'])
            review.save()

            for image in images:
                Photo.objects.create(review_id=review, image=image, landscape_id=landscape)
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
        result = es_search(query, location=location, activities=activities, accessibilities=accessibilities)
        response = JsonResponse({"data": result, 'is_success': True})
        return response


def es_search(query='', **filters):
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


@login_required()
@csrf_exempt
def add_like(request, landscape_name_slug):
    try:
        landscape = Landscape.objects.get(slug=landscape_name_slug)
    except Landscape.DoesNotExist:
        return redirect('/landscape/')
    if request.method == 'PUT':
        data = json.loads(request.body)
        liked = data.get('liked', True)
        if liked:
            saved_landscapes.objects.update_or_create(landscape_id=landscape, user_id=request.user)
        else:
            saved_landscapes.objects.filter(user_id=request.user, landscape_id=landscape).delete()
        return JsonResponse({'data': {'message': 'like updated'}, 'is_success': True})
    else:
        raise Http404
