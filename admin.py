from django.contrib import admin
# from storages.backends.s3boto3 import S3Boto3Storage

from .models import User

# Register your models here.
admin.site.register(User)
# S3Boto3Storage.site.register(User)
# Register your models here.
