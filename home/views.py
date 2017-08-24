from django.shortcuts import render, get_object_or_404
from .models import Product
from products import urls as products_urls




# Create your views here.
def get_index(request):
    return render(request, 'index.html')

def do_search(request):
    products = Products.objects.filter(name__contains=request.GET['q'])
    return render(request, 'results.html', {'Products':products})