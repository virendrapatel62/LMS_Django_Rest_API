from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class StaticFilesStorage(S3Boto3Storage):
    location = settings.STATIC_FILES_LOCATION


class MediaFilesStorage(S3Boto3Storage):
    location = settings.MEDIA_FILES_LOCATION
