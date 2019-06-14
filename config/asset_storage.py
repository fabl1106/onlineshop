from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    location = ""
    bucket_name = 'onlineshop.lushjuice.com'
    region_name = 'ap-northeast-2'
    custom_domain = 's3.%s.amazonaws.com/%s' % (region_name,bucket_name)
    file_overwrite = False