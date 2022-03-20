from django.shortcuts import render
import json
import urllib
from utils import utils


# Create your views here.

def homepage(request):
    if request.method == 'GET':
        location = request.COOKIES.get('location')
        if location:
            location = json.loads(urllib.parse.unquote(location))
        visited_results = utils.es_search('', activities=[], accessibilities=[])
        location_results = utils.es_search('', location=location, activities=[], accessibilities=[])
        context_dict = {"visited_results": visited_results, "location_results": location_results}
        return render(request, 'home/homepage.html', context=context_dict)
