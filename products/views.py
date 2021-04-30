from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.


def products_view(request):
    products_db = Product.objects.all()
    products_list = []

    for product in products_db:
        products_obj = {
            'id': product.id,
            'title': product.title,
            'description': product.description,
            'price': product.price
        }
        products_list.append(products_obj)

        context = {
            'products': products_list
        }

    return render(request, "products.html", context)
