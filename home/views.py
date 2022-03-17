from django.shortcuts import render

# Create your views here.

def homepage(request):

    context_dict = {}
    
    context_dict['landscapes'] = [{"id": 3, "name": "Ben Nevis", "description": "Ben Nevis couldn\u2019t be any more dramatic, with a summit often veiled by clouds, and dustings of pure white snow. Once an enormous active volcano, it's now a silent giant watching over the glacial valleys and lochs of the land.", "address": "Loch Lomond, Loch Lomond and The Trossachs National Park, Alexandria G83 8QZ Scotland", "slug": "sjfkdj", "images": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/BenNevis2005.jpg/1920px-BenNevis2005.jpg", "activities": ["fishing"], "accessibilities": [], "is_active": True, "latitude": 80.0, "review": {"average_rating": 3.5, "count": 2}}, {"id": 1, "name": "Glen Coe", "description": "Glen Coe is Scotland\u2019s most famous, and most romantic glen.\r\n\r\nSome landscapes are worthy of a postcard, but not a blockbuster film. Glen Coe on the other hand is truly filmic and featured in one of the Harry Potter films. Its awe-inspiring scenery and Machiavellian history has long been an inspiration for creatives, and to visit is life enriching.", "address": "Loch Lomond, Loch Lomond and The Trossachs National Park, Alexandria G83 8QZ Scotland", "slug": "glen-coe", "images": "https://media-cdn.tripadvisor.com/media/photo-s/0f/18/48/99/lost-valley-glen-coe.jpg", "activities": [], "accessibilities": ["hi"], "is_active": True, "latitude": 80.0, "review": {"average_rating": 4.0, "count": 1}}, {"id": 2, "name": "Loch Lomond", "description": "A new story begins.. Set amidst 400 acres of Scottish countryside on the bonnie banks of Loch Lomond, the historical 17th century Baronial mansion has been lovingly restored and sets the scene for a legendary story to unfold. Discover our reimagined suites and bedrooms, impeccable dining, championship golf and award-winning spa; a stay at Cameron House Hotel is set to be an unforgettable experience for everyone to enjoy.", "address": "Loch Lomond, Loch Lomond and The Trossachs National Park, Alexandria G83 8QZ Scotland", "slug": "loch-lohmond", "images": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/06/80/1e/29/loch-katrine.jpg?w=2000&h=-1&s=1", "activities": ["boating", "hiking", "fishing"], "accessibilities": ["wheelchair"], "is_active": True, "latitude": 90.0, "review": {"average_rating": 0.0, "count": 0}}, {id: "4", "name": "The Quiraing", "description": "This is an essential walk for any photographer as it passes though some of the most spectacular landscapes in Scotland. As part of the Trotternish ridge it has been formed by a massive landslip which has created high cliffs, hidden plateaus and pinnacles of rock.","address": "North of Skye - Trotternish","images": "https://upload.wikimedia.org/wikipedia/commons/a/a7/South_over_the_Quiraing%2C_Isle_of_Skye.jpg","activities": ["hiking"],"accessibilities": ["parking"], "is_active": True, "latitude": 90.0, "review": {"average_rating": 0.0, "count": 0}}, {"name": "Newburgh Beach","description": "Just 20 minutes north of Aberdeen, you find yourself at a wonderful sandy beach and home of an extensive sand dune system at the mouth of the Ythan River. A must see is the 400 strong colony of seals at the mouth of Ythan River.","address": "20 minutes North of Aberdeen, Newburgh","images": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/14/2b/f3/60/img-20180816-131447-largejpg.jpg?w=1000&h=-1&s=1","activities": [""],"accessibilities": ["parking"], "is_active": True, "latitude": 80.0, "review": {"average_rating": 4.0, "count": 1}}, {"id": 5, "name": "Loch Ness","description": "Loch Ness is a large freshwater loch in the Scottish Highlands extending for approximately 37 kilometres southwest of Inverness. It takes its name from the River Ness, which flows from the northern end.","address": "Inverness","images": "https://www.visitinvernesslochness.com/sites/default/files/2021-09/DJI_0271__1920.jpg","activities": ["swimming"],"accessibilities": ["kid's area, parking, toilets"],"is_active": True, "latitude": 90.0, "review": {"average_rating": 3.0, "count": 0}}


  ]


    #context_dict['landscapes'] = {'title': 'Loch Lomond', 'image': "{% static 'images/lochLomond.jpg' %}", 'views': 100}
    

    if request.method == 'GET':
        return render(request, 'home/homepage.html', context=context_dict)






