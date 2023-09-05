import os
from decouple import config, Csv
from .common import Common


class Production(Common):
    INSTALLED_APPS = Common.INSTALLED_APPS
    SECRET_KEY = config('DJANGO_SECRET_KEY')
    ALLOWED_HOSTS = config('DJANGO_ALLOWED_HOSTS', cast=Csv())
    ADMIN_URL = config('DJANGO_ADMIN_URL')

    # Site
    # https://docs.djangoproject.com/en/2.0/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = ["*"]
    INSTALLED_APPS += ("gunicorn", 'cloudinary_storage', 'cloudinary',)

    # CSRF
    CSRF_TRUSTED_ORIGINS = config("CSRF_TRUSTED_ORIGINS", cast=Csv())

    # CORS
    CORS_URLS_REGEX = r"^/api/.*$"
    CORS_ALLOWED_ORIGINS = config("CORS_ALLOWED_ORIGINS", cast=Csv())
    CORS_ALLOW_ALL_ORIGINS = config("CORS_ALLOW_ALL_ORIGINS", default=False, cast=bool)
    CORS_ALLOW_METHODS = (
        "DELETE",
        "GET",
        "OPTIONS",
        "PATCH",
        "POST",
        "PUT",
    )
    CORS_ALLOW_HEADERS = (
        "accept",
        "authorization",
        "content-type",
        "user-agent",
        "x-csrftoken",
        "x-requested-with",
    )

    # Cloudinary
    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': config("CLOUDINARY_CLOUD_NAME"),
        'API_KEY': config("CLOUDINARY_API_KEY"),
        'API_SECRET': config("CLOUDINARY_API_SECRET"),
    }

    STORAGES = {
        "default": {
            "BACKEND": "cloudinary_storage.storage.RawMediaCloudinaryStorage",
        },
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        },
    }

    