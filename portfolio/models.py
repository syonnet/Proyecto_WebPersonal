from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=100, verbose_name="Titulo")
    description=models.TextField(verbose_name="Descripcion")
    image=models.ImageField(verbose_name="Imagen", upload_to='project')
    
    link = models.URLField(max_length=200, blank=True, null=True, verbose_name='Enlace')
    
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')

    class Meta:
        verbose_name='proyecto'
        verbose_name_plural='proyectos'
        ordering=['-created']
        
    def __str__(self) :
        return self.title
        