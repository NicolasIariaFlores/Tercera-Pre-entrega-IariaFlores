from django.shortcuts import render, redirect
from . import models
#from form import BebidaForm

def index(request):
    bebidas = models.Bebida.objects.all()
    snacks = models.Snack.objects.all()
    chocolates = models.Chocolate.objects.all()
    datos = {"bebidas" : bebidas, "snacks" : snacks, "chocolates" : chocolates}
    return render(request, "producto/index_producto.html", datos)

#def chocolates(request):
 #   chocolates = models.Chocolate.objects.all()
  #  dato = {"chocolates" : chocolates}
   # return render(request, "templates/chocolate.html", dato)

# def crear_productos(request):
#     if request.method == "POST":
#         form = BebidaForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("producto/index_producto.html")
#     else:
#         form = BebidaForm()
#     return render(request, "producto/crear.html", {"form" : form})