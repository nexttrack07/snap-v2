import os

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = "prodsnap"
AWS_S3_ENDPOINT_URL = "https://prodsnap.nyc3.digitaloceanspaces.com"
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400"
}
AWS_LOCATION = "https://prodsnap.nyc3.digitaloceanspaces.com"

DEFAULT_FILE_STORAGE = "config.cdn.backends.MediaRootS3Boto3Storage"
STATICFILES_STORAGE = "config.cdn.backends.StaticRootS3Boto3Storage"
