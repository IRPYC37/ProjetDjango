from django import forms
from .models import *


class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'code', 'description', 'price', 'price_ht', 'price_ttc']


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
        fields = ['name', 'contact_info', 'description']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['supplier']

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

    def __init__(self, *args, **kwargs):
        supplier = kwargs.pop('supplier', None)
        super().__init__(*args, **kwargs)
        if supplier:
            self.fields['product'].queryset = Product.objects.filter(suppliers=supplier)

class ProductSupplierForm(forms.ModelForm):
    class Meta:
        model = ProductSupplier
        fields = ['product', 'price']

ProductSupplierFormSet = forms.inlineformset_factory(Supplier, ProductSupplier, form=ProductSupplierForm, extra=1, can_delete=True)