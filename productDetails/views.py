from django.shortcuts import render, get_object_or_404
from .models import ProductDetails, Gender

# Create your views here.
def productDetails(request):
    productsDetails=ProductDetails.objects.all()
    return render(request, "productDetails/productDetails.html", {'listproductsDetails': productsDetails})

def gender(request, genderId):
    #gender=Gender.objects.get(id=genderId)
    gender=get_object_or_404(Gender, id=genderId)
    productsDetails=ProductDetails.objects.filter(genders=gender)
    return render(request, "productDetails/gender.html", {'listproductsDetails': productsDetails})