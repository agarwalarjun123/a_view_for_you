from django.shortcuts import render

# Create your views here.

def homepage(request):

    context_dict = {}
    context_dict['landscapes'] = [{"id": 3, "name": "Ben Nevis", "description": "Ben Nevis couldn\u2019t be any more dramatic, with a summit often veiled by clouds, and dustings of pure white snow. Once an enormous active volcano, it's now a silent giant watching over the glacial valleys and lochs of the land.", "address": "", "slug": "sjfkdj", "images": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/06/80/1e/29/loch-katrine.jpg?w=2000&h=-1&s=1", "activities": ["fishing"], "accessibilities": [], "is_active": True, "latitude": 80.0, "review": {"average_rating": 3.5, "count": 2}}, {"id": 1, "name": "Glen Coe", "description": "Glen Coe is Scotland\u2019s most famous, and most romantic glen.\r\n\r\nSome landscapes are worthy of a postcard, but not a blockbuster film. Glen Coe on the other hand is truly filmic and featured in one of the Harry Potter films. Its awe-inspiring scenery and Machiavellian history has long been an inspiration for creatives, and to visit is life enriching.", "address": "glencoe address", "slug": "glen-coe", "images": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/06/80/1e/29/loch-katrine.jpg?w=2000&h=-1&s=1", "activities": [], "accessibilities": ["hi"], "is_active": True, "latitude": 80.0, "review": {"average_rating": 4.0, "count": 1}}, {"id": 2, "name": "Loch Lomond", "description": "A new story begins.. Set amidst 400 acres of Scottish countryside on the bonnie banks of Loch Lomond, the historical 17th century Baronial mansion has been lovingly restored and sets the scene for a legendary story to unfold. Discover our reimagined suites and bedrooms, impeccable dining, championship golf and award-winning spa; a stay at Cameron House Hotel is set to be an unforgettable experience for everyone to enjoy.", "address": "Loch Lomond, Loch Lomond and The Trossachs National Park, Alexandria G83 8QZ Scotland", "slug": "loch-lohmond", "images": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/06/80/1e/29/loch-katrine.jpg?w=2000&h=-1&s=1", "activities": ["boating", "hiking", "fishing"], "accessibilities": ["wheelchair"], "is_active": True, "latitude": 90.0, "review": {"average_rating": 0.0, "count": 0}}]


    #context_dict['landscapes'] = {'title': 'Loch Lomond', 'image': "{% static 'images/lochLomond.jpg' %}", 'views': 100}
    

    if request.method == 'GET':
        return render(request, 'home/homepage.html', context=context_dict)






