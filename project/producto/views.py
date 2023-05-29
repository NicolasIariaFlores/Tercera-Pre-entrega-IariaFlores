from django.shortcuts import render
from . import models

def index(request):
    bebidas = models.Bebida.objects.all()
    chocolates = models.Chocolate.objects.all()
    snacks = models.Snack.objects.all()
    datos = {"bebidas" : bebidas, "chocolates" : chocolates, "snacks" : snacks}
    return render(request, "producto/index_producto.html", datos)