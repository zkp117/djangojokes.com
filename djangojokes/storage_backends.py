from storages.backends.s3boto3 import S3Boto3Storage
class StaticStorage(S3Boto3Storage):
    """ Class for storing static files. """
    location = 'static'
    default_acl = 'public-read'
    file_overwrite = False

class PublicMediaStorage(S3Boto3Storage):
    location = "media"  # Ensures files go to "media/" instead of "static/"
    default_acl = "public-read"  # Makes avatars publicly accessible
    file_overwrite = False  # Prevents overwriting existing files

class PrivateMediaStorage(S3Boto3Storage):
    """ Class for storing private media files. """
    location = 'media/private'
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False