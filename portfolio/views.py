from django.shortcuts import render

from.models import Project


# Create your views here.

def portfolio(request):
    #consultando la lista de modelos mediante el modelo
    projects=Project.objects.all()
    return render(request, "portfolio/portfolio.html", {'projects':projects})