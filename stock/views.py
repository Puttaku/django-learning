from django.shortcuts import render
from .models import Product
def index(request):
    products = Product.objects.all()
    return render(request, 'front/index.html', {"products": products})

def about(request):
    return render(request, 'front/about.html')

def contact(request):
    return render(request, 'front/contact.html')

# Create your views here.
