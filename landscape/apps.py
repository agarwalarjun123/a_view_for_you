from django.apps import AppConfig
import logging


logger = logging.getLogger(__name__)

class LandscapeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'landscape'
    landscape_max_length = 200    
    def ready(self):
        from utils.utils import connect_es
        try:
            es = connect_es()
            self.es = es
        except ValueError as e:
            ### need to raise error ideally!!
            logger.error(e)
