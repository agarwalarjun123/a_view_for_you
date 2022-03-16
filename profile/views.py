
from django.shortcuts import render
from landscape.models import Landscape, Review
from authentication.models import User
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def profile(request):
    if request.method == 'GET':
        return render(request, 'profile/profile.html')


class ProfileLikes(View):
    @method_decorator(login_required)
    def get(self, request):
        profile_likes = Review.objects.all()

        return render(request, 'profile/profiles.html', {'Profilelikes': profile_likes})

class ProfileReviews(View):
    @method_decorator(login_required)
    def get(self, request):
        profile_reviews = Review.objects.all()

        return render(request, 'profile/profiles.html', {'ProfileReviews': profile_reviews})


