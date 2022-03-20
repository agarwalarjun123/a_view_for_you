from django.db import models
from elasticsearch import Elasticsearch
from django.conf import settings
from django.apps import apps as django_apps
from django.core.files import File
from urllib import request, parse


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def connect_es():
    es = Elasticsearch(settings.ES_URL,
                       ca_certs=settings.ES_CERT_PATH, verify_certs=False)
    if not es.ping():
        raise ValueError("Elasticsearch connection failed.")
    return es


def es_search(query='', **filters):
    # query
    es_query = {
        'bool': {
            'must': [
                {
                    'term': {
                        'is_active': True,
                    }
                }],
        }
    }
    if query:
        es_query['bool']['must'].append({
            'multi_match': {
                'fields': ['*'],
                'query': query,
                'fuzziness': 'AUTO'
            }
        })

    # location
    if 'location' in filters and filters['location']:
        es_query['bool']['must'].append({
            'geo_distance': {
                "distance": django_apps.get_app_config('landscape').GEO_DISTANCE,
                "location": filters['location'],
            }
        })

    additional_filters = len(filters['activities']) > 0 or len(filters['accessibilities']) > 0
    es_query['bool']['should'] = [] if additional_filters else None
    es_query['bool']['minimum_should_match'] = 1 if additional_filters else None

    # add the filter to the query if exists
    if len(filters['activities']) > 0:
        es_query['bool']['should'].append({
            'terms': {
                'activities': filters['activities'],
            }})

    if len(filters['accessibilities']) > 0:
        es_query['bool']['should'].append({
            'terms': {
                'accessibilities': filters['accessibilities'],
            }})
    es = django_apps.get_app_config('landscape').es

    SORTING = [
        {'review.average_rating': {'order': 'desc'}},
        {'review.count': {'order': 'desc'}}
    ]
    result = es.search(index=settings.ES_INDEX,
                       query=es_query, sort=SORTING)
    result = [data['_source'] for data in result.body['hits']['hits']]
    return result


def read_image_from_url(url):
    result = request.urlretrieve(url)
    file_name = parse.urlparse(url).path.split('/')[-1]
    return File(open(result[0], 'rb')), file_name


def roundRating(rating):
    number = int(rating * 100 / 5)
    hundreds = (number % 1000) // 100
    tens = (number % 100) // 10
    percentage = "" if hundreds == 0 else "1"
    return percentage
