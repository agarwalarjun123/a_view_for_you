from django.db import models
from elasticsearch import Elasticsearch
from django.conf import settings
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