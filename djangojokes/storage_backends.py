from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    """ Class for storing static files. """
    location = 'static'
    default_acl = 'public-read'
    file_overwrite = True

class PublicMediaStorage(S3Boto3Storage):
    # This sets the base location for media files to be saved
    location = 'media/public/avatar'
    file_overwrite = False  # Do not overwrite existing files with the same name

class PrivateMediaStorage(S3Boto3Storage):
    """ Class for storing private media files. """
    location = 'media/private'
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False