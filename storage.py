from storages.backends.s3boto import S3BotoStorage
class mystorage(S3BotoStorage):
base_url = 'zappa-nb517gz2u.s3.amazonaws.com'