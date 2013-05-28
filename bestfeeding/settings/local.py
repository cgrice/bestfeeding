# settings/local.py 
from .base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': dj_database_url.parse(get_env_variable('DJANGO_DATABASE_URL'))
}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
}
