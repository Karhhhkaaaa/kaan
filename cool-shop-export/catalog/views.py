from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from . import models


def index(request: HttpRequest) -> HttpResponse:
    products = models.Product.objects.all()
    context = {'products': products}

    return render(request, 'catalog/index.html', context)
