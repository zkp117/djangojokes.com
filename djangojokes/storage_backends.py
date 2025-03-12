from storages.backends.s3boto3 import S3Boto3Storage
class StaticStorage(S3Boto3Storage):
    """ Class for storing static files. """
    location = 'static'
    default_acl = 'public-read'
    file_overwrite = True

class PublicMediaStorage(S3Boto3Storage):
    """ Class for storing public media files. """
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = False

class PrivateMediaStorage(S3Boto3Storage):
    """ Class for storing private media files. """
    location = 'media/private'
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False

class AvatarStorage(S3Boto3Storage):
    location = 'media/public/avatars'
    default_acl = 'public-read'
    file_overwrite = False