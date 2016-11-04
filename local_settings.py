import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'secretgoeshere'

# SITES
SITE_ID = 1

ADMINS = (
    ('JOHNDOE', 'EMAIL@EXAMPLE.COM'),
)

MANAGERS = (
    ('JOHNDOE', 'EMAIL@EXAMPLE.COM')
)

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'EXAMPLE',
        'USER': 'EXAMPLE',
        'PASSWORD': 'secretgoeshere',
    }
}

# CACHE
# CACHES = {
#    'default': {
#        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
#    }
# }

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
        'TIMEOUT': 86400,
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}


# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "127.0.0.1:6379:1",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }


# SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# SESSION_CACHE_ALIAS = "default"

CACHEOPS_FAKE = True

# Media
MEDIA_ROOT = "/var/www/media/"
MEDIA_URL = 'https://EXAMPLE.COM/media/'

# static
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = 'https://EXAMPLE.COM/static/'
STATIC_ROOT = '/var/www/static/'
# COMPRESS_ROOT = ""

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# haystack
# HAYSTACK_CONNECTIONS = {
#    'default': {
#        'ENGINE': 'xapian_backend.XapianEngine',
#        'PATH': os.path.join(os.path.dirname(__file__), 'xapian_index'),
#        'INCLUDE_SPELLING': True,
#    },
# }

HAYSTACK_ITERATOR_LOAD_PER_QUERY = 90000000

# Test Email
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_HOST = 'localhost'
# EMAIL_PORT = 587
# DEFAULT_FROM_EMAIL='John Doe <johndow@example.com>'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_HOST_USER = 'postmaster@EXAMPLE.COM'
EMAIL_HOST_PASSWORD = 'passwordgoeshere'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'EXAMPLE <support@EXAMPLE.COM>'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['EXAMPLE.COM', 'www.EXAMPLE.COM']
CRISPY_FAIL_SILENTLY = not DEBUG
TEST_RUNNER = 'django.test.runner.DiscoverRunner'
