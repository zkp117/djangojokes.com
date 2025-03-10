from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    """ Class for storing static files. """
    location = 'static'
    default_acl = 'public-read'
    file_overwrite = True

class PublicMediaStorage(S3Boto3Storage):
    location = "media"
    default_acl = "public-read"  # Make media files public
    file_overwrite = False
    custom_domain = f"{'django-jokes2025.s3.amazonaws.com'}"


class PrivateMediaStorage(S3Boto3Storage):
    """ Class for storing private media files. """
    location = 'media/private'
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False