import os
import django
# setting up environment and loading up models
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'a_view_for_you.settings')
django.setup()
from django.core.files import File
from urllib import request,parse
from landscape.models import Landscape,Photo
def populate():
    populate_landscapes()

def read_image_from_url(url):
    result = request.urlretrieve(url)    
    file_name = parse.urlparse(url).path.split('/')[-1]
    print(file_name)
    return File(open(result[0], 'rb')), file_name

def populate_landscapes():
    landscapes = [
         {
      "name": "Ben Nevis",
      "description": "Ben Nevis couldn't be any more dramatic, with a summit often veiled by clouds, and dustings of pure white snow. Once an enormous active volcano, it's now a silent giant watching over the glacial valleys and lochs of the land.",
      "address": "scotland",
      "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/06/80/1e/29/loch-katrine.jpg?w=2000&h=-1&s=1",
      "activities": [
        "fishing","hiking"
      ],
      "images": ["https://dynamic-media-cdn.tripadvisor.com/media/photo-o/06/80/1e/29/loch-katrine.jpg?w=2000&h=-1&s=1"],
      "accessibilities": [],

      "latitude": 80,
      "longitude" : 90,
      "reviews":[]
    }, 
    {
      "name": "Glen Coe",
      "description": "Glen Coe is Scotland's most famous, and most romantic glen.Some landscapes are worthy of a postcard, but not a blockbuster film. Glen Coe on the other hand is truly filmic and featured in one of the Harry Potter films. Its awe-inspiring scenery and Machiavellian history has long been an inspiration for creatives, and to visit is life enriching.",
      "address": "glencoe address",
      "images": ["https://dynamic-media-cdn.tripadvisor.com/media/photo-o/06/80/1e/29/loch-katrine.jpg?w=2000&h=-1&s=1"],
      "activities": ["boating"],
      "accessibilities": [
        "wheelchair"
      ],
        "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/06/80/1e/29/loch-katrine.jpg?w=2000&h=-1&s=1",

      "latitude": 80,
      "longitude": 90,
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
        "fishing"
      ],
      "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/06/80/1e/29/loch-katrine.jpg?w=2000&h=-1&s=1",
      "accessibilities": [
        "wheelchair"
      ],
      "latitude": 90,
      "longitude": 80,
      "reviews": []
    }
    ]
    for landscape in landscapes:
        landscape_doc = {key: landscape[key] for key in list(set(landscape.keys()) & set(['name','description','activities','accessibilities','latitude','longitude']))}
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