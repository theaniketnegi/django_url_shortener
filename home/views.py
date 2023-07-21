from django.shortcuts import render, redirect
import uuid
from .models import LinkInfo
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'index.html')

def shorten(request):
    if(request.method=="POST"):
        link = request.POST['url']
        link_id = str(uuid.uuid4())[:6]
        shortened_link = LinkInfo(link=link, link_id=link_id)
        shortened_link.save()
        return HttpResponse(link_id)

def redirectUrl(request, id):
    link_obj = LinkInfo.objects.get(link_id=id)
    return redirect(link_obj.link)