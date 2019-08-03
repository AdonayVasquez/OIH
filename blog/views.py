from django.shortcuts import render
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Entrada, Article, Aspirantes
from django.views.generic import TemplateView, ListView, DetailView
from django.template import loader, RequestContext, Template
from .forms import ContactForm
#class HomeView(TemplateView):
    #inicio = "inicio.html"

class ListaView(ListView):
    template_name = 'articulos.html'
    model = Entrada

class EntradaDetailView(DetailView):
    template_name = 'articulo_detalle.html'
    model = Entrada

def get_redirected(queryset_or_class, lookups, validators):
    """
    Calls get_object_or_404 and conditionally builds redirect URL
    """
    obj = get_object_or_404(queryset_or_class, **lookups)
    for key, value in validators.items():
        if value != getattr(obj, key):
            return obj, obj.get_absolute_url()
    return obj, None

def my_view(request, slug, id):
    article, article_url = get_redirected(Article, {'pk': id}, {'slug': slug})
    if article_url:
        return redirect(article_url)


class DetailsView(DetailView):
    template_name = 'detail.html'
    context_object_name = "blog_detail"

    def get_object(self):
        _id = self.kwargs.get("id")
        return get_object_or_404(Entrada, id=_id)

def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            contact.save()
            
    else:
        form = ContactForm()
    template = loader.get_template('inicio.html')
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))