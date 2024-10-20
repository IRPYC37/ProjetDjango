from django import forms
from .models import *


class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)


class ProductForm(forms.ModelForm):
    suppliers = forms.ModelMultipleChoiceField(
        queryset=Supplier.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Product
        fields = "__all__"



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
    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Supplier
        fields = ['name', 'contact_info', 'description', 'products']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']  # Assurez-vous que ces champs sont corrects

    def __init__(self, *args, **kwargs):
        supplier = kwargs.pop('supplier', None)  # Récupérer le fournisseur si fourni
        super(OrderItemForm, self).__init__(*args, **kwargs)
        if supplier:
            # Filtrer les produits par fournisseur
            self.fields['product'].queryset = supplier.supplied_products.all()


class ProductSupplierForm(forms.ModelForm):
    class Meta:
        model = ProductSupplier
        fields = ['price']