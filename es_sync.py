from django.forms.models import model_to_dict

import os
import django
# setting up environment and loading up models
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'a_view_for_you.settings')
django.setup()
from landscape.models import Landscape,Review, Photo
from django.conf import settings
from django.db.models import Avg,Count
from utils.utils import connect_es
import os

def read_from_db():
    es = connect_es()
    if not es.indices.exists(index=settings.ES_INDEX):
        es.indices.create(index=settings.ES_INDEX)
    else:
        es.delete_by_query(index=settings.ES_INDEX, query={
            'match_all': {}
        })
    es.indices.put_mapping( body = {
            'properties': {
                'location': {
                   'type': 'geo_point'
                }
        }
    },index = settings.ES_INDEX)
    landscapes = Landscape.objects.all()
    for landscape in landscapes:

        landscape_doc = model_to_dict(landscape, fields=[
                 'id', 'name', 'description', 'address', 'slug', 'activities', 'accessibilities', 'is_active', 'created_at', 'updated_at'])
        landscape_doc['location'] = {
            'lat': landscape.latitude,
            'lon': landscape.longitude
        }
        landscape_doc['image'] = settings.MEDIA_URL + landscape.image.name
        review = read_review(landscape_doc['id'])
        landscape_doc['review'] = review
        es.index(index=settings.ES_INDEX, document=landscape_doc)

def read_review(landscape_id):
    result = Review.objects.filter(landscape_id = landscape_id).aggregate(average_rating = Avg('rating',default = 0), count = Count('id'))
    print(result)
    result["average_rating"]=0 if result["average_rating"] is None else result["average_rating"]
    return result
if __name__ == '__main__':
    read_from_db()
