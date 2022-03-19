
from django.shortcuts import render
import landscape
from landscape.models import Landscape, Review
from authentication.models import User
from landscape.views import roundRating
from django.contrib.auth.decorators import login_required

@login_required()
def show_profile(request):
    if request.method == 'GET':
        return render(request, 'profile/profile.html')


# try to filter reviews made by user

@login_required()
def show_profile_reviews(request):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}
    try:
        profile_reviews = Review.objects.filter(
            user_id=request.user.id).order_by('-visit_date')
        for r in profile_reviews:
            r.rating = roundRating(r.rating)
        context_dict['profile_reviews'] = profile_reviews
    except Review.DoesNotExist:
        # do nothing
        context_dict['profile_reviews'] = None
    return render(request, 'profile/profile.html', context=context_dict)


# try to filter landscapes liked by user
"""
@login_required()
def show_profile_likes(request):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}
    try:
        # to do: filter
        profile_likes = Landscape.objects.filter()
        context_dict['profile_likes'] = profile_likes
    except Review.DoesNotExist:
        # do nothing
        context_dict['profile_likes'] = None
    return render(request, 'profile/profile.html', context=context_dict)
"""


