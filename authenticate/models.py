from datetime import datetime
from django.db import models
from django.utils import timezone
import os 

def filepath(request, filename):
  old_filename = filename
  timeNow = datetime.now().strftime('%Y%m%d%H%:&M:%S')
  filename = "%s%s" %(timeNow, old_filename)
  return os.path.join('uploads/', filename)

# Create your models here.
class Book(models.Model):
  title = models.CharField(max_length=200, unique=False, default="")
  author = models.CharField(null=True, max_length=200)
  status = models.CharField(null=True, default="available", max_length=200)
  description = models.TextField(null=True)
  cover = models.ImageField(upload_to=filepath, null=True, blank=True)
  category = models.CharField(max_length=200, null=False, default="computer")
  created_at = models.DateTimeField(default=timezone.now) 

  def __str__(self):
    return self.title

  class Meta: 
    verbose_name_plural = "Books"
