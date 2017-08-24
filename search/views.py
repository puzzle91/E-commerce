from django.shortcuts import render


# Create your views here.
from django.shortcuts import render, get_object_or_404


def get_index(request):
    return render(request, 'index.html')

def product_search(request):
    products = Product.objects.filter(name__contains=request.GET['q'])
    return render(request, 'results.html', {'products': products})