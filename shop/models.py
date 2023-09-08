from django.db import models

# Create your models here.
class Shop(models.Model):
    title=models.CharField(max_length=100, verbose_name="Titulo")
    gender=models.CharField(max_length=100, verbose_name="Genero")
    image=models.ImageField(verbose_name="Imagen", upload_to="Shop")
    price=models.IntegerField(verbose_name="Precio")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"
        ordering=["-created"]
    
    def __str__(self):
        return self.title