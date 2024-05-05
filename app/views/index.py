from django.shortcuts import render
from django.views.decorators.cache import never_cache


@never_cache
def index(request):
    return render(request, 'index.html')


@never_cache
def catalog(request):
    return render(request, 'catalog.html')
