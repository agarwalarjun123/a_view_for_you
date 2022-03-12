from django.shortcuts import redirect, render
from django.conf import settings
from django.http import JsonResponse
from django.apps import apps as django_apps
from landscape.models import Landscape, Photo, Review
from authentication.models import User
from landscape.forms import ReviewForm
from django.apps import apps
from django.contrib.auth.decorators import login_required

def index(request):

    context_dict = {}
    context_dict['activities'] = apps.get_app_config('landscape').activities
    context_dict['accessibilities'] = apps.get_app_config(
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
        for r in reviews:
            r.rating = roundRating(r.rating)
        context_dict['reviews'] = reviews
        context_dict['landscape'] = landscape
    except Landscape.DoesNotExist:
        # We get here if we didn't find the specified reviews.
        # Don't do anything -
        # the template will display the "no reviews" message for us.
        context_dict['landscape'] = None
        context_dict['reviews'] = None
    # Go render the response and return it to the client.
    return render(request, 'landscape/landscape.html', context=context_dict)

@login_required()
def add_review(request, landscape_name_slug):
    print("*ADD REVIEW")
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
            user = User.objects.first()
            # TODO: replace this for the logged user
            review.user_id = user
            review.save()

            for image in images:
                print("**Image added")
                photo = Photo.objects.create(review_id =review, image = image)
        
            return redirect('/landscape/')
        print(form.errors)
        error_message = form.errors

    context_dict = {}
    context_dict['form'] = form
    context_dict['landscape'] = landscape
    context_dict['activities'] = apps.get_app_config('landscape').activities
    context_dict['accessibilities'] = apps.get_app_config('landscape').accessibilities
    context_dict['error_message'] = error_message
    return render(request, 'landscape/add_review.html', context=context_dict)


def search(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')
        location = {k: float(request.GET.get(k))
                    for k in ['lat', 'lon']} if request.GET.get('lat') else None
        activities = request.GET.get('activities').split(',') if request.GET.get(
            'activities') and len(request.GET.get('activities').split(',')) > 0 else []
        accessibilities = request.GET.get('accessibilities').split(',') if request.GET.get(
            'accessibilities') and len(request.GET.get('accessibilities').split(',')) > 0 else []
        es_query = {
            'bool': {
                'must': [{
                    'multi_match': {
                        'fields': ['*'],
                        'query': query
                    }
                },
                    {
                        'term': {
                            'is_active': True,
                        }
                }],
            }

        }
        if location:
            es_query['bool']['must'].append({
                'geo_distance': {
                    "distance": django_apps.get_app_config('landscape').GEO_DISTANCE,
                         "location": location,
                }   
            })
        additional_filters = len(activities) > 0 or len(accessibilities) > 0
        es_query['bool']['should'] = [] if additional_filters else None
        es_query['bool']['minimum_should_match'] = 1 if additional_filters else None
        # add the filter to the query if exists
        if len(activities) > 0:
            es_query['bool']['should'].append({
                'terms': {
                    'activities': activities,
                }})
        if len(accessibilities) > 0:
            es_query['bool']['should'].append({
                'terms': {
                    'accessibilities': accessibilities,
                }})
        es = django_apps.get_app_config('landscape').es
        result = es.search(index=settings.ES_INDEX, query=es_query)
        result = [data['_source'] for data in result.body['hits']['hits']]
        response = JsonResponse({"data": result, 'is_success': True})
        return response


def roundRating(rating):
    number = int(rating*100/5)
    hundreds = (number % 1000) // 100
    tens = (number % 100) // 10
    percentage = "" if hundreds == 0 else "1"
    return percentage
