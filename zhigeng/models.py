from django.db import models
#
import os,django
# django.setup()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# class Upload(models.Model):
#     tok = models.CharField(max_length=168)
#     file_name = models.CharField(max_length=168)
#     platform = models.CharField(max_length=64)
#     environ = models.CharField(max_length=64)
#     # environ = models.CharField(max_length=64)

class Upload_list(models.Model):
    tok = models.CharField(max_length=168)
    file_name = models.CharField(max_length=168)
    platform = models.CharField(max_length=64)
    environ = models.CharField(max_length=64)