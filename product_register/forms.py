from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class ProductOptionForm(forms.ModelForm):
    class Meta:
        model = ProductOption
        fields = "__all__"
    
    def __init__(self,*args,**kwargs):
        super(ProductOptionForm, self).__init__(*args,**kwargs)
        self.fields['Product'].empty_label= "Select"
