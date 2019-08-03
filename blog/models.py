from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
# Create your models here.

class Entrada(models.Model):
    titulo = models.CharField(max_length=200)
    #contenido = RichTextField()
    contenido = RichTextUploadingField(blank=True, null=True)
    slug = models.SlugField(editable=False)

    def __unicode__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)
        super(Entrada, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

class Article(models.Model):
  def get_absolute_url(self):
        return reverse('article', kwargs={'slug': self.slug, 'id':self.id})


class Aspirantes(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.nombre

class Archivos(models.Model):
    titulo = models.CharField(max_length=50)
    archivo = models.FileField(null=True, blank=True ,upload_to='router_specifications')
    archivo2 = models.BinaryField(null=True, blank=True )
    descripcion = models.TextField(max_length=500)


    def __str__(self):
        return self.titulo
    
    
