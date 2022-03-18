from django.test import TestCase
from unittest.mock import Mock, patch
from utils import utils
from .models import Landscape,Photo
from urllib import request,parse
from django.core.files import File
# Create your tests here.


def mocked_f(**kwargs):
    return []
@patch.object(utils,'es_search',Mock(return_value=[]))

class LandscapeTest(TestCase):
    def setUp(self):
        populate_landscapes()
    def test_homepage_up(self):
        """tests that the response status_code is 200"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def tests_homepage_headers(self):
        """tests that the response should not contain the headers"""
        response = self.client.get('/')
        self.assertNotContains(response,'Most Visited Landscapes')
        self.assertNotContains(response,'Landscapes near you')
    def tests_landscape(self):
        """tests that the response contains the landscape page and status code = 200 for existing landscape"""
        response = self.client.get('/landscape/loch-lomond/')
        self.assertEqual(response.status_code, 200)
    def tests_landscape_not_present(self):
        """tests that the response redirects with status code 302 to landscape page"""
        response = self.client.get('/landscape/loch/')
        self.assertEqual(response.status_code, 302)
    


def read_image_from_url(url):
    result = request.urlretrieve(url)    
    file_name = parse.urlparse(url).path.split('/')[-1]
    return File(open(result[0], 'rb')), file_name

def populate_landscapes():
    landscapes = [
         {
      "name": "Ben Nevis",
      "description": "Ben Nevis couldn't be any more dramatic, with a summit often veiled by clouds, and dustings of pure white snow. Once an enormous active volcano, it's now a silent giant watching over the glacial valleys and lochs of the land.",
      "address": "Loch Lomond, Loch Lomond and The Trossachs National Park, Alexandria G83 8QZ Scotland",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/BenNevis2005.jpg/1920px-BenNevis2005.jpg",
      "activities": [
        "fishing","hiking"
      ],
      "images": ["https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/BenNevis2005.jpg/1920px-BenNevis2005.jpg"],
      "accessibilities": [],

      "latitude": 80,
      "longitude" : 90,
      "reviews":[]
    }, 
    {
      "name": "Glen Coe",
      "description": "Glen Coe is Scotland's most famous, and most romantic glen.Some landscapes are worthy of a postcard, but not a blockbuster film. Glen Coe on the other hand is truly filmic and featured in one of the Harry Potter films. Its awe-inspiring scenery and Machiavellian history has long been an inspiration for creatives, and to visit is life enriching.",
      "address": "Loch Lomond, Loch Lomond and The Trossachs National Park, Alexandria G83 8QZ Scotland",
      "images": ["https://thumbs.dreamstime.com/b/remote-mountain-cottage-glencoe-picture-postcard-scottish-highlands-79753771.jpg"],
      "activities": ["boating"],
      "accessibilities": [
        "wheelchair"
      ],
        "image": "https://thumbs.dreamstime.com/b/remote-mountain-cottage-glencoe-picture-postcard-scottish-highlands-79753771.jpg",

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
        "fishing"
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

      "latitude": 57,
      "longitude": -6,
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
      "images": ["https://www.visitinvernesslochness.com/sites/default/files/2021-09/DJI_0271__1920.jpg","https://cdn.britannica.com/77/2977-050-6CEA9F21/Loch-Ness-Highlands-of-Scotland-head-monastery.jpg","https://ichef.bbci.co.uk/news/976/cpsprodpb/E751/production/_107971295_lochnessone.jpg","https://ichef.bbci.co.uk/news/976/cpsprodpb/E751/production/_107971295_lochnessone.jpg","https://ichef.bbci.co.uk/news/976/cpsprodpb/E751/production/_107971295_lochnessone.jpg"],
      "activities": ["swimming"],
      "accessibilities": ["kids-area, parking, toilets"],
        "image": "https://www.visitinvernesslochness.com/sites/default/files/2021-09/DJI_0271__1920.jpg",

      "latitude": 57,
      "longitude": -2,
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