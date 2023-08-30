from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin): #clase extendida de configuracion
    readonly_fields=('created','updated')
    

admin.site.register(Project,ProjectAdmin)
