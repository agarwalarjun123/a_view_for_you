from django.http import HttpResponse
from django.shortcuts import redirect, render
from authentication.models import User
from landscape.forms import ReviewForm

from landscape.models import Landscape, Review
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    context_dict = {}
    landscapes = Landscape.objects.all().order_by('name')[:5]
    context_dict['landscapes'] = landscapes
    print("**Landscapes")
    return render(request, 'landscape/index.html', context=context_dict)

def show_landscape(request, landscape_name_slug):
    # Create a context dictionary which we can pass 
    # to the template rendering engine. 
    context_dict = {}
    try:
        landscape = Landscape.objects.get(slug = landscape_name_slug )
        reviews = Review.objects.filter(landscape_id=landscape.id).order_by('-visit_date')[:5]
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
        landscape = Landscape.objects.get(slug = landscape_name_slug)
    except Landscape.DoesNotExist:
        landscape = None
    
    if landscape is None:
        return redirect('/landscape/')

    form = ReviewForm()
    if request.method == 'POST':
        print ("POST")
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.landscape_id = landscape
            user = User.objects.first()
            #TODO: replace this for the logged user
            review.user_id = user
            review.save()
            return redirect('/landscape/')
        else:
            print(form.errors)
    context_dict = {'form': form, 'landscape': landscape}
    return render(request, 'landscape/add_review.html', context = context_dict)
