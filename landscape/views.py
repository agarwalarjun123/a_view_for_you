from django.shortcuts import redirect, render
from django.conf import settings
from django.http import JsonResponse
from django.apps import apps as django_apps
from landscape.models import Landscape, Review
from authentication.models import User
from landscape.forms import ReviewForm


def index(request):
    context_dict = {}
    context_dict['activities'] = ["Boating", "Camping", "Fishing", "Hiking", "Swimming" ]
    context_dict['accessibilities'] = ["Kid's area", "Parking", "Pet friendly", "Toilets", "Wheelchair"]
    
    if request.method == 'GET':
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


def add_review(request, landscape_name_slug):
    print("*ADD REVIEW")
    try:
        landscape = Landscape.objects.get(slug=landscape_name_slug)
    except Landscape.DoesNotExist:
        landscape = None

    if landscape is None:
        return redirect('/landscape/')

    form = ReviewForm()
    if request.method == 'POST':
        print("POST")
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.landscape_id = landscape
            user = User.objects.first()
            # TODO: replace this for the logged user
            review.user_id = user
            review.save()
            return redirect('/landscape/')
        else:
            print(form.errors)
    context_dict = {'form': form, 'landscape': landscape}
    return render(request, 'landscape/add_review.html', context=context_dict)


def search(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')
        activities = request.GET.get('activities').split(',') if request.GET.get('activities') and len(request.GET.get('activities').split(',')) > 0 else []
        accessibilities = request.GET.get('accessibilities').split(',') if request.GET.get('accessibilities') and len(request.GET.get('accessibilities').split(',')) > 0 else []
        ## base query
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
        additional_filters = len(activities)> 0 or len(accessibilities)>0
        es_query['bool']['should'] = [] if additional_filters else None
        es_query['bool']['minimum_should_match'] = 1 if additional_filters else None
        ## add the filter to the query if exists
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
    percentage += str(tens) +"0"
    return percentage