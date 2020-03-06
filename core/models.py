from django.db import models

# Create your models here.
class Url(models.Model):
  long_url  = models.CharField(max_length=100)
  short_url = models.CharField(max_length=100)
  clicks    = models.IntegerField(default=0)

  def __str__(self):
      return self.long_url