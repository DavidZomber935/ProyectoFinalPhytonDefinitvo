from django.urls import path
from . import views

urlpatterns = [
    path('',views.productDetails, name="productDetails"),
    path('gender/<int:genderId>/', views.gender, name="gender"),
]

