from django.shortcuts import render
from landscape.models import saved_landscapes, Review
from landscape.views import roundRating
from django.contrib.auth.decorators import login_required

@login_required()
def show_profile(request):
    context_dict = {}
    if request.method == 'GET':
        try:
            profile_likes = saved_landscapes.objects.filter(user_id_id=request.user.id)
            context_dict['profile_likes'] = profile_likes
        except saved_landscapes.DoesNotExist:
            # do nothing
            context_dict['profile_likes'] = None

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
    #return render(request, 'profile/profile.html')

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
@login_required()
def show_profile_likes(request):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}
    try:
        profile_likes = Like.objects.filter(
            user_id=request.user.id).order_by('-visit_date')
        context_dict['profile_likes'] = profile_likes
    except Review.DoesNotExist:
        # do nothing
        context_dict['profile_likes'] = None
    return render(request, 'profile/profile.html', context=context_dict)