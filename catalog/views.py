from django.shortcuts import render
from .models import Product

def home_view(request):
    products = Product.objects.all()[:8]  # عرض أول 8 منتجات فقط
    return render(request, 'home.html', {'products': products})
