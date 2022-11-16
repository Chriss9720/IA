from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from .models import Members

from .forms import Form

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def lista(request):
    cdx = {
        'lista': Members.objects.all()
    }
    template = loader.get_template('lista.html')
    return HttpResponse(template.render(cdx))

def add(request):
    if (request.method == 'GET'):
        cdx = {
            'form': Form()
        }
        return render(request, 'add.html', cdx)
    
    elif request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
        else:
            cdx = {
                'form': form
            }
            return render(request, 'lista.html', cdx)
    else:
        pass

def deleted(request, id):
    member = Members.objects.filter(id = id)
    member.delete()
    cdx = {
        'lista': Members.objects.all()
    }
    return redirect('lista')

def update(request, id):
    member = Members.objects.filter(id = id).first()
    if request.method == 'GET':
        cdx = {
            'form': Form(instance=member)
        }
        return render(request, 'add.html', cdx)
    elif request.method == 'POST':
        form = Form(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('lista')