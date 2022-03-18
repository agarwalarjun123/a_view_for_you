from django.shortcuts import render

from landscape.views import es_search

# Create your views here.

def homepage(request):

    
    if request.method == 'GET':
        location = {k: float(request.GET.get(k))
                    for k in ['lat', 'lon']} if request.GET.get('lat') else None
        visited_results = es_search('', activities = [], accessibilities = [])
        location_results = es_search('', location = location, activities = [], accessibilities = [])
        context_dict = {"visited_results": visited_results, "location_results": location_results}
        return render(request, 'home/homepage.html', context=context_dict)






