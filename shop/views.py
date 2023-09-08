from django.shortcuts import render
from .models import Shop

# Create your views here.
def shop(request):
    shop=Shop.objects.all()
    return render(request, "shop/shop.html", {'listShop':shop})