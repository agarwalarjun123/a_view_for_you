from django.shortcuts import redirect, render
from django.conf import settings
from django.http import JsonResponse
from django.apps import apps as django_apps
from landscape.models import Landscape, Review
from authentication.models import User
from landscape.forms import ReviewForm


def index(request):
    # context_dict = {}
    # landscapes = Landscape.objects.all().order_by('name')[:5]
    # context_dict['landscapes'] = landscapes
    # print("**Landscapes")
    if request.method == 'GET':
        return render(request, 'landscape/index.html')


def show_landscape(request, landscape_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}
    try:
        landscape = Landscape.objects.get(slug=landscape_name_slug)
        reviews = Review.objects.filter(
            landscape_id=landscape.id).order_by('-visit_date')[:5]
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
        print(query)
        es = django_apps.get_app_config('landscape').es
        result = es.search(index=settings.ES_INDEX, query={
            'bool': {
                'must': {
                    'multi_match': {
                        'fields': ['*'],
                        'query': query
                    }
                },
                'filter': {
                    'term': {
                        'is_active': True
                    }
                }
            }

        })
        result = result.body['hits']['hits']
        result = [data['_source'] for data in result]
        response = JsonResponse({"data": result, 'is_success': True})
        return response
