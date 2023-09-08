from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Gender(models.Model):
    name=models.CharField(max_length=50, verbose_name="Nombre de genero")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")

    class Meta:
        verbose_name="Genero"
        verbose_name_plural="Generos"
        ordering=["name"]

    def __str__(self):
        return self.name

class ProductDetails(models.Model):
    title=models.CharField(max_length=100, verbose_name="Titulo")
    review=models.TextField(verbose_name="Reseña")
    image=models.ImageField(verbose_name="Imagen",upload_to="productDetails")
    author=models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    genders=models.ManyToManyField(Gender, verbose_name="Generos")
    price=models.IntegerField(verbose_name="Precio")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")

    class Meta:
        verbose_name="Reseña"
        verbose_name_plural="Reseñas"
        ordering=["-created"]
    
    def __str__(self):
        return self.title
 
