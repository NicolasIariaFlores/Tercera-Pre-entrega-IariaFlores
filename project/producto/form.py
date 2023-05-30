from django import forms
from . import models

class ChocolateForm(forms.ModelForm):
    class Meta:
        model = models.Chocolate()
        fields = "__all__"

class BebidaForm(forms.ModelForm):
    class Meta: 
        model = models.Bebida()
        fields = "__all__"

class SnackForm(forms.ModelForm):
    class Meta:
        model = models.Snack()
        fields = "__all__" 