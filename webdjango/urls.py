"""webdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#from blog.views import HomeView
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from blog.views import ListaView, EntradaDetailView, my_view, DetailsView, contacto
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
    #path('home/', HomeView.as_view()),
    path('', TemplateView.as_view(template_name="inicio.html")),
    path('inicio', TemplateView.as_view(template_name="inicio.html")),
    path('contactoo', TemplateView.as_view(template_name="contacto.html")),
    #path('articulo', TemplateView.as_view(template_name="articulo.html")),
    path('articulos', ListaView.as_view()),
    #path('entrada/<slug:slug>,<int:id>/', EntradaDetailView.as_view()),
    #path('entrada/<slug:slug>', EntradaDetailView.as_view())
    #path('<slug:slug>,<int:id>/', my_view, name='article'),
    path('entrada/<int:id>/', DetailsView.as_view(), name="detail"),
    path('contacto', contacto, name="detail"),
   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()