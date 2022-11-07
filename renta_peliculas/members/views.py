from django.http import HttpResponse
from django.template import loader
from .models import Members

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def lista(request):
    cdx = {
        'lista': Members.objects.all()
    }
    template = loader.get_template('lista.html')
    return HttpResponse(template.render(cdx))