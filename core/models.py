from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Url(models.Model):
  long_url  = models.CharField(max_length=100)
  short_url = models.CharField(max_length=100)
  clicks    = models.IntegerField(default=0)
  owner     = models.ForeignKey(User, on_delete=models.CASCADE, related_name='urls')

  def __str__(self):
      return self.long_url