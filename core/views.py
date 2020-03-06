from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import messages

from django.views.generic import ListView, DeleteView, View
from core.models import Url

import string
import random 

# Create your views here.
class UrlShortenerView(ListView):
  queryset            = Url.objects.all().order_by('-id')
  context_object_name = 'all_urls'
  template_name       = 'home.html'

  def post(self, request):
    form_data = request.POST

    long_url  = form_data['long_url']
    short_url = form_data['short_url'].replace(" ", "_")

    if(not short_url):
      short_url = ''.join(random.choices(string.ascii_lowercase+string.digits, k=8))

    exists = Url.objects.filter(short_url=short_url)

    if(not exists):
      new_url = Url(long_url=long_url, short_url=short_url)
      new_url.save()
    
    else:
      messages.error(request, 'This short URL already Exists Please try again.')
    
    return redirect('/urls/')

class UrlDeleteView(View):
  def post(self, request, urlid):
    query = Url.objects.get(id=urlid)
    print(urlid)
    query.delete()
    return redirect('/urls/')

class UrlRedirectView(View):
  def get(self, request, target):

    shortened_object = get_object_or_404(Url, short_url=target)
    destination      = shortened_object.long_url
     
    shortened_object.clicks+=1
    shortened_object.save()
    
    return redirect(destination)