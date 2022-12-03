from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import members



# Create your views here.
def index(request):
    mymembers = members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))


def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    member = members(firstname=x, lastname=y)
    member.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    member = members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))


def update(request, id):
  mymember = members.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    member = members.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()
    return HttpResponseRedirect(reverse('index'))


