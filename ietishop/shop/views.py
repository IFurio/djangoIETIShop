from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.
def product_list(request):
    productes = Producte.objects.all()
    return render(request, "product_list.html", {"productes":productes})

def category_list(request):
    categories = Categoria.objects.all()
    return render(request, "category_list.html", {"categories":categories})

def products_category(request, category_id):
    categoria = Categoria.objects.get(pk=categoria_id)
    products = Producte.objects.filter(categoria=categoria)
    # Hacer algo con los productos obtenidos
    return render(request, "product_list.html", {"productes":productes})
    