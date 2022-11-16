from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista', views.lista, name='lista'),
    path('add', views.add, name='add'),
    path('deleted/<id>', views.deleted, name='deleted'),
    path('update/<id>', views.update, name='update'),
]