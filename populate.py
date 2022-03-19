import os
import django
# setting up environment and loading up models
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'a_view_for_you.settings')
django.setup()
from django.core.files import File
from urllib import request,parse
from landscape.models import Landscape,Photo,Review
def populate():
    populate_landscapes()

def read_image_from_url(url):
    result = request.urlretrieve(url)    
    file_name = parse.urlparse(url).path.split('/')[-1]
    return File(open(result[0], 'rb')), file_name

def populate_reviews():
  reviews = [
    {
      "title": "Amazing hike!",
      "description": "I went on april and i had a great time. It is quite challenging but the view is amazing. ",
      "rating": "5",
      "visit_date": "2021-04-21",
      "facilities": [],
      "activities": ["fishing"],
      "user_id": "",
      "landscape_id": Landscape.objects.filter(name="Ben Nevis"),
    }
  ]
def populate_landscapes():
    landscapes = [
         {
      "name": "Ben Nevis",
      "description": "Ben Nevis couldn't be any more dramatic, with a summit often veiled by clouds, and dustings of pure white snow. Once an enormous active volcano, it's now a silent giant watching over the glacial valleys and lochs of the land.",
      "address": "Loch Lomond, Loch Lomond and The Trossachs National Park, Alexandria G83 8QZ Scotland",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/BenNevis2005.jpg/1920px-BenNevis2005.jpg",
      "activities": [
        "fishing","hiking", "camping"
      ],
      "images": ["https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/BenNevis2005.jpg/1920px-BenNevis2005.jpg"],
      "accessibilities": [],

<<<<<<< Updated upstream
      "latitude": 56.7973, 
      "longitude" : -5.0034,
      "reviews":[]
=======
      "latitude": 80,
      "longitude" : 90,
      "reviews":[{
        "title": "Amazing hike!",
        "description": "I went on april and i had a great time. It is quite challenging but the view is amazing. ",
        "rating": "5",
        "visit_date": "2021-04-21",
        "facilities": [],
        "activities": ["fishing"],
        "user_id": ""
      }]
>>>>>>> Stashed changes
    }, 
    {
      "name": "Glencoe",
      "description": "Glen Coe is Scotland's most famous, and most romantic glen. Some landscapes are worthy of a postcard, but not a blockbuster film. Glen Coe on the other hand is truly filmic and featured in one of the Harry Potter films. Its awe-inspiring scenery and Machiavellian history has long been an inspiration for creatives, and to visit is life enriching.",
      "address": "Loch Lomond, Loch Lomond and The Trossachs National Park, Alexandria G83 8QZ Scotland",
      "images": ["https://thumbs.dreamstime.com/b/remote-mountain-cottage-glencoe-picture-postcard-scottish-highlands-79753771.jpg"],
      "activities": ["boating, hiking, camping"],
      "accessibilities": [
        "wheelchair"
      ],
        "image": "https://thumbs.dreamstime.com/b/remote-mountain-cottage-glencoe-picture-postcard-scottish-highlands-79753771.jpg",

      "latitude": 56.6830, 
      "longitude": -5.1020,
      "reviews":[]
    },
    {
      "name": "Loch Lomond",
      "description": "A new story begins.. Set amidst 400 acres of Scottish countryside on the bonnie banks of Loch Lomond, the historical 17th century Baronial mansion has been lovingly restored and sets the scene for a legendary story to unfold. Discover our reimagined suites and bedrooms, impeccable dining, championship golf and award-winning spa; a stay at Cameron House Hotel is set to be an unforgettable experience for everyone to enjoy.",
      "address": "Loch Lomond, Loch Lomond and The Trossachs National Park, Alexandria G83 8QZ Scotland",
      "images": ["https://dynamic-media-cdn.tripadvisor.com/media/photo-o/06/80/1e/29/loch-katrine.jpg?w=2000&h=-1&s=1"],
      "activities": [
        "boating",
        "hiking",
        "fishing", "swimming"
      ],
      "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/06/80/1e/29/loch-katrine.jpg?w=2000&h=-1&s=1",
      "accessibilities": [
        "wheelchair"
      ],
      "latitude": 28.4809,
      "longitude": 77.0803,
      "reviews": []
    },
    {
      "name": "Cairngorms",
      "description": "The Cairngorms (Scottish Gaelic: Am Monadh Ruadh) are a mountain range in the eastern Highlands of Scotland closely associated with the mountain Cairn Gorm. The Cairngorms became part of Scotland's second national park (the Cairngorms National Park) on 1 September 2003.[2] Although the Cairngorms give their name to, and are at the heart of, the Cairngorms National Park, they only form one part of the national park, alongside other hill ranges such as the Angus Glens and the Monadhliath, and lower areas like Strathspey.",
      "address": "Highland, Aberdeenshire and Moray, Scotland",
      "images": ["https://upload.wikimedia.org/wikipedia/commons/7/7e/The-cairngorms-from-geal-charn.jpg"],
      "activities": [
        "boating",
        "hiking",
        "fishing", "camping"
      ],
      "image": "https://upload.wikimedia.org/wikipedia/commons/7/7e/The-cairngorms-from-geal-charn.jpg",
      "accessibilities": [
        "wheelchair"
      ],
      "latitude": 28.4107,
      "longitude": 77.0424,
      "reviews": []
    },
        {
      "name": "The Quiraing",
      "description": "This is an essential walk for any photographer as it passes though some of the most spectacular landscapes in Scotland. As part of the Trotternish ridge it has been formed by a massive landslip which has created high cliffs, hidden plateaus and pinnacles of rock.",
      "address": "North of Skye - Trotternish",
      "images": ["https://upload.wikimedia.org/wikipedia/commons/a/a7/South_over_the_Quiraing%2C_Isle_of_Skye.jpg"],
      "activities": ["hiking"],
      "accessibilities": ["parking"],
        "image": "https://upload.wikimedia.org/wikipedia/commons/a/a7/South_over_the_Quiraing%2C_Isle_of_Skye.jpg",

      "latitude": 57.6440, 
      "longitude": -6.2654,
      "reviews":[]
    }, 
    {
    "name": "Newburgh Beach",
      "description": "Just 20 minutes north of Aberdeen, you find yourself at a wonderful sandy beach and home of an extensive sand dune system at the mouth of the Ythan River. A must see is the 400 strong colony of seals at the mouth of Ythan River.",
      "address": "20 Minutes north of Aberdeen, Newburgh",
      "images": ["https://dynamic-media-cdn.tripadvisor.com/media/photo-o/14/2b/f3/60/img-20180816-131447-largejpg.jpg?w=1000&h=-1&s=1"],
      "activities": [""],
      "accessibilities": ["parking"],
        "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/14/2b/f3/60/img-20180816-131447-largejpg.jpg?w=1000&h=-1&s=1",

      "latitude": 57.3087,
      "longitude": -1.9913,
      "reviews":[]
    },
    {
    "name": "Loch Ness",
      "description": "Loch Ness is a large freshwater loch in the Scottish Highlands extending for approximately 37 kilometres southwest of Inverness. It takes its name from the River Ness, which flows from the northern end.",
      "address": "Inverness",
      "images": ["https://www.visitinvernesslochness.com/sites/default/files/2021-09/DJI_0271__1920.jpg"],
      "activities": ["swimming", "boating"],
      "accessibilities": ["kids-area, parking, toilets"],
        "image": "https://www.visitinvernesslochness.com/sites/default/files/2021-09/DJI_0271__1920.jpg",

      "latitude": 57.3353, 
      "longitude": -4.4193,
      "reviews":[]
    },
    {
    "name": "Old Man of Storr",
      "description": "The Storr is a rocky hill on the Trotternish peninsula of the Isle of Skye in Scotland. The hill presents a steep rocky eastern face overlooking the Sound of Raasay, contrasting with gentler grassy slopes to the west.",
      "address": "Isle of Skye",
      "images": ["https://www.myhighlands.de/wp-content/uploads/2020/05/Old-Man-Panorama-01-1536x864.jpg.webp"],
      "activities": ["hiking"],
      "accessibilities": ["parking", "pet-friendly"],
        "image": "https://www.myhighlands.de/wp-content/uploads/2020/05/Old-Man-Panorama-01-1536x864.jpg.webp",

      "latitude": 57.5073, 
      "longitude": -6.1836,
      "reviews":[]
    },
    {
     "name": "Galloway International Dark Sky Park",
      "description": "A Dark Sky Park is a place with exceptionally dark night skies. It is also a place where people have committed to keeping those skies dark, by controlling light pollution.",
      "address": "Galloway Forest Patk, Dumfries and Galloway",
      "images": ["https://forestryandland.gov.scot/images/Blog/2024160.jpg"],
      "activities": ["hiking", "camping"],
      "accessibilities": ["parking", "toilets"],
        "image": "https://forestryandland.gov.scot/images/Blog/2024160.jpg",

      "latitude": 55.1099, 
      "longitude": -4.4367,
      "reviews":[]
    },
     {
     "name": "Arthurs Seat",
      "description": "Arthur's Seat is an ancient volcano which is the main peak of the group of hills in Edinburgh, Scotland, which form most of Holyrood Park.",
      "address": "Edinburgh",
      "images": ["https://www.walkhighlands.co.uk/lothian/1_2/1_2_2l.JPG"],
      "activities": ["hiking"],
      "accessibilities": ["parking"],
        "image": "https://www.walkhighlands.co.uk/lothian/1_2/1_2_2l.JPG",

      "latitude": 55.9444, 
      "longitude": -3.1615,
      "reviews":[]
    },
     {
     "name": "The Cobbler",
      "description": "The Cobbler is an 884 metres mountain located near the head of Loch Long in Argyll and Bute, Scotland. It is a Corbett, and is an important site for rock climbing in the Southern Highlands.",
      "address": "Highlands",
      "images": ["https://www.lovefromscotland.co.uk/wp-content/uploads/2018/12/The-Cobbler-Ben-Arthur-Needle-1.jpg"],
      "activities": ["hiking"],
      "accessibilities": ["parking"],
        "image": "https://www.lovefromscotland.co.uk/wp-content/uploads/2018/12/The-Cobbler-Ben-Arthur-Needle-1.jpg",

      "latitude": 56.2137, 
      "longitude": -4.8079,
      "reviews":[]
    },
    {
     "name": "Steall Falls",
      "description": "The spectacular waterfall known variously as An Steall Bàn, Steall Waterfall or Steall Falls is situated in Glen Nevis near Fort William, Highland, Scotland.",
      "address": "Highlands",
      "images": ["https://www.wildlochaber.com/sites/wildlochaber.com/files/walking/steall_gorge_02.jpg"],
      "activities": ["hiking"],
      "accessibilities": ["parking"],
        "image": "https://www.wildlochaber.com/sites/wildlochaber.com/files/walking/steall_gorge_02.jpg",

      "latitude": 56.7709, 
      "longitude": -4.9795,
      "reviews":[]
    },
    {
     "name": "The Devils Pulpit",
      "description": "Waterfall & stream flowing between towering rock formations, accessed by a steep stone staircase.",
      "address": "Glasgow, G63 9QJ",
      "images": ["https://i2.wp.com/naturesoffgridtreasures.com/wp-content/uploads/2017/09/naslovna.jpg?fit=1500%2C720&ssl=1"],
      "activities": ["hiking"],
      "accessibilities": [""],
        "image": "https://i2.wp.com/naturesoffgridtreasures.com/wp-content/uploads/2017/09/naslovna.jpg?fit=1500%2C720&ssl=1",

      "latitude": 56.0344, 
      "longitude": -4.4138,
      "reviews":[]
    }
    ]
    for landscape in landscapes:
        landscape_doc = {key: landscape[key] for key in list(set(landscape.keys()) & set(['name','address','description','activities','accessibilities','latitude','longitude']))}
        landscape_doc = Landscape(**landscape_doc)
        if landscape['image']:
            file,name = read_image_from_url(landscape['image'])
            landscape_doc.image.save(name,file)
        landscape_doc.save()
        for image in landscape["images"]:
            file,name = read_image_from_url(image)
            image = Photo(landscape_id = landscape_doc)
            image.image.save(name,file)
            image.save()
            


if __name__ == "__main__":
    populate()