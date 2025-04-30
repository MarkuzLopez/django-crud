#forms with model and template

from  django import forms
from .models import Product

#step 2 for create form with template
#create form based in model
class ProductForm(forms.ModelForm):
    class Meta:
      model = Product
      fields = ['name', 'product']