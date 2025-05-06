#forms with model and template

from  django import forms
from .models import Product, Estudiante

#step 2 for create form with template
#create form based in model
class ProductForm(forms.ModelForm):
    class Meta:
      model = Product
      fields = ['name', 'product']

# Relaciones entre modelos (OneToMany, ManyToMany) con admin y formularios.
# paso-3 crear formulario
class EstudianteForm(forms.ModelForm):
  class Meta: 
    model =  Estudiante
    fields = ['nombre', 'cursos']