from django import forms
from .models import *


class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ["price_ttc", "status"]


class ProductItemForm(forms.ModelForm):
    class Meta:
        model = ProductItem
        fields = "__all__"


class ProductAttributeForm(forms.ModelForm):
    class Meta:
        model = ProductAttribute
        fields = "__all__"


class ProductAttributeValueForm(forms.ModelForm):
    class Meta:
        model = ProductAttributeValue
        fields = "__all__"

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = "__all__"
