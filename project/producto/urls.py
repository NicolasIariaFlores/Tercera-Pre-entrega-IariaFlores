from django.urls import path
from . import views

app_name = "productos"

urlpatterns = [
    path('', views.index, name="index"),
    #path("crear/", crear_productos, name="crear")
    #path('chocolate/', views.chocolates, name="chocolate"),
]