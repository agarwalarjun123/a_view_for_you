from django.apps import AppConfig
import logging


logger = logging.getLogger(__name__)


class LandscapeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'landscape'
    activities = [
        {
            "display_name": "Boating",
            "name": "boating",
        }, 
        {
            "display_name": "Camping",
            "name": "camping"
        },
        {
            "display_name": "Fishing",
            "name": "fishing"
        },
        {
            "display_name": "Hiking",
            "name": "hiking"
        },
        {
            "display_name":  "Swimming",
            "name":  "swimming"
        }]
    accessibilities = [
        {
            "display_name": "Kid's area",
            "name": "kids-area"
        },
        {
            "display_name": "Parking",
            "name":"parking"
        },
        {
            "display_name": "Pet Friendly",
            "name": "pet-friendly"
        },
        {
            "display_name": "Toilets",
            "name": "toilets"
        },
        {
            "display_name": "Wheelchair",
            "name": "wheelchair"
        }
    ]
    landscape_max_length = 200

    def ready(self):
        from utils.utils import connect_es
        try:
            es = connect_es()
            self.es = es
        except ValueError as e:
            # need to raise error ideally!!
            logger.error(e)
