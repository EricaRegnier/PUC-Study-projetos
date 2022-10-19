from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
     path('', views.index, name='index'),
    path('registro', views.registroUsuario, name='registro'),
    path('login', views.loginUsuario, name='login'),
    path('menu', views.menu, name='menu'),
    path('registroAvaliacao', views.registroAvaliacao, name='registroAvaliacao'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico')))
]
