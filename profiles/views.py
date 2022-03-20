from django.shortcuts import redirect, render
from landscape.models import saved_landscapes, Review
from django.contrib.auth.decorators import login_required

from profiles.form import ProfileForm

@login_required()
def show_profile(request):
    context_dict = {}
    if request.method == 'GET':
        context_dict = {}
        profile_likes = set()
        try:
            profile_saved_landscapes = saved_landscapes.objects.filter(
                user_id=request.user.id).select_related('landscape_id')
            for like in profile_saved_landscapes:
                # like.landscape_id is not a integer but a Landscape instance!
                profile_likes.add(like.landscape_id)
            #profile_likes is a set of landscapes
            context_dict['profile_likes'] = profile_likes
        except saved_landscapes.DoesNotExist:
            # do nothing
            context_dict['profile_likes'] = None

        try:
            profile_reviews = Review.objects.filter(
                user_id=request.user.id).order_by('-visit_date')
            context_dict['profile_reviews'] = profile_reviews
        except Review.DoesNotExist:
            # do nothing
            context_dict['profile_reviews'] = None

    return render(request, 'profile/profile.html', context=context_dict)
    #return render(request, 'profile/profile.html')

# try to filter users who likes this landscape
def show_landscape_likes(request):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}
    landscape_likes = set()
    try:
        saved_landscape_likes = saved_landscapes.objects.filter(
            landscpae_id=request.landscape.id)
        for like in saved_landscape_likes:
            #like.user_id is not a integer but a user instance!
            landscape_likes.add(like.user_id)
        #landscape_likes is a set of users
        context_dict['landscape_likes'] = landscape_likes
    except saved_landscapes.DoesNotExist:
        # do nothing
        context_dict['landscape_likes'] = None
    return render(request, 'profile/profile.html', context=context_dict)

# try to filter users who reviewed this landscape
def show_landscape_reviews(request):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}
    landscape_review = set()
    try:
        saved_landscape_reviews = Review.objects.filter(
            landscpae_id=request.landscape.id)
        for review in saved_landscape_reviews:
            #like.user_id is not a integer but a user instance!
            landscape_review.add(review.user_id)
        #landscape_reviews is a set of users
        context_dict['landscape_review'] = landscape_review
    except saved_landscapes.DoesNotExist:
        # do nothing
        context_dict['landscape_review'] = None
    return render(request, 'profile/profile.html', context=context_dict)

@login_required()
def edit_profile(request):
    profileForm = {}
    if request.method == 'GET':
        profileForm = ProfileForm()
    if request.method == 'POST':
        profileForm = ProfileForm(request.POST)
        if profileForm.is_valid():
            if 'profile_image' in request.FILES:
                request.user.profile_image = request.FILES['profile_image']
                #request.user.introduction = "changed"
            if not request.POST['introduction'] is None:
                request.user.introduction = request.POST['introduction']
            request.user.save()
            return redirect("profile:profile")
    return render(request, 'profile/edit_profile.html', {'form': profileForm})
