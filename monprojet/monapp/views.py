from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import *
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.forms import BaseModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from .forms import *
from .models import *

# Create your views here.


class HomeView(TemplateView):
    template_name = "monapp/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["titreh1"] = "Hello"
        context["param"] = self.kwargs.get("param", "")
        return context

    def post(self, request, **kwargs):
        return render(request, self.template_name)


class ProductListView(ListView):
    model = Product
    template_name = "monapp/list_products.html"
    context_object_name = "products"

    def get_queryset(self):
        # Surcouche pour filtrer les résultats en fonction de la recherche
        # Récupérer le terme de recherche depuis la requête GET
        query = self.request.GET.get("search")
        if query:
            # Filtre les produits par nom (insensible à la casse)
            return Product.objects.filter(name__icontains=query)
        # Si aucun terme de recherche, retourner tous les produits
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context["titremenu"] = "Liste des produits"
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "monapp/detail_product.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context["titremenu"] = "Détail produit"
        return context


# Ajout du décorateur login_required à une CBV
@method_decorator(login_required, name="dispatch")
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "monapp/new_product.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        product = form.save()
        return redirect("product-detail", product.id)


# Ajout du décorateur login_required à une CBV
@method_decorator(login_required, name="dispatch")
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "monapp/update_product.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        product = form.save()
        return redirect("product-detail", product.id)


# Ajout du décorateur login_required à une CBV
@method_decorator(login_required, name="dispatch")
class ProductDeleteView(DeleteView):
    model = Product
    template_name = "monapp/delete_product.html"
    success_url = reverse_lazy("product-list")


class ProductItemListView(ListView):
    model = ProductItem
    template_name = "monapp/list_product_items.html"
    context_object_name = "productitems"

    def get_queryset(self):
        query = self.request.GET.get("search")
        if query:
            return ProductItem.objects.filter(color__icontains=query)
        return ProductItem.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProductItemListView, self).get_context_data(**kwargs)
        context["titremenu"] = "Liste des déclinaisons"
        return context


class ProductItemDetailView(DetailView):
    model = ProductItem
    template_name = "monapp/detail_product_item.html"
    context_object_name = "productitem"

    def get_context_data(self, **kwargs):
        context = super(ProductItemDetailView, self).get_context_data(**kwargs)
        context["titremenu"] = "Détail déclinaison"
        # Récupérer les attributs associés à cette déclinaison
        context["attributes"] = self.object.attributes.all()
        return context


# Ajout du décorateur login_required à une CBV
@method_decorator(login_required, name="dispatch")
class ProductItemCreateView(CreateView):
    model = ProductItem
    form_class = ProductItemForm
    template_name = "monapp/new_product_item.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        product_item = form.save()
        return redirect("product-item-detail", product_item.id)


# Ajout du décorateur login_required à une CBV
@method_decorator(login_required, name="dispatch")
class ProductItemUpdateView(UpdateView):
    model = ProductItem
    form_class = ProductItemForm
    template_name = "monapp/update_product_item.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        product_item = form.save()
        return redirect("product-item-detail", product_item.id)


# Ajout du décorateur login_required à une CBV
@method_decorator(login_required, name="dispatch")
class ProductItemDeleteView(DeleteView):
    model = ProductItem
    template_name = "monapp/delete_product_item.html"
    success_url = reverse_lazy("product-item-list")


class ProductAttributeListView(ListView):
    model = ProductAttribute
    template_name = "monapp/list_product_attributes.html"
    context_object_name = "productattributes"

    def get_queryset(self):
        query = self.request.GET.get("search")
        if query:
            return ProductAttribute.objects.filter(name__icontains=query)
        return ProductAttribute.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProductAttributeListView, self).get_context_data(**kwargs)
        context["titremenu"] = "Liste des attributs"
        return context


class ProductAttributeDetailView(DetailView):
    model = ProductAttribute
    template_name = "monapp/detail_product_attribute.html"
    context_object_name = "productattribute"

    def get_context_data(self, **kwargs):
        context = super(ProductAttributeDetailView, self).get_context_data(**kwargs)
        context["titremenu"] = "Détail attribut"
        context["values"] = ProductAttributeValue.objects.filter(
            product_attribute=self.object
        ).order_by("position")
        return context


# Ajout du décorateur login_required à une CBV
@method_decorator(login_required, name="dispatch")
class ProductAttributeCreateView(CreateView):
    model = ProductAttribute
    form_class = ProductAttributeForm
    template_name = "monapp/new_product_attribute.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        product_attribute = form.save()
        return redirect("product-attribute-detail", product_attribute.id)


# Ajout du décorateur login_required à une CBV
@method_decorator(login_required, name="dispatch")
class ProductAttributeUpdateView(UpdateView):
    model = ProductAttribute
    form_class = ProductAttributeForm
    template_name = "monapp/update_product_attribute.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        product_attribute = form.save()
        return redirect("product-attribute-detail", product_attribute.id)


# Ajout du décorateur login_required à une CBV
@method_decorator(login_required, name="dispatch")
class ProductAttributeDeleteView(DeleteView):
    model = ProductAttribute
    template_name = "monapp/delete_product_attribute.html"
    success_url = reverse_lazy("product-attribute-list")


class ProductAttributeValueVListView(ListView):
    model = ProductAttributeValue
    template_name = "monapp/list_products_attribute_value.html"
    context_object_name = "products_attribute_value"

    def get_queryset(self):
        # Surcouche pour filtrer les résultats en fonction de la recherche
        # Récupérer le terme de recherche depuis la requête GET
        query = self.request.GET.get("search")
        if query:
            # Filtre les produits par nom (insensible à la casse)
            return ProductAttributeValue.objects.filter(value__icontains=query)
        # Si aucun terme de recherche, retourner tous les produits
        return ProductAttributeValue.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProductAttributeValueVListView, self).get_context_data(**kwargs)
        context["titremenu"] = "Liste des attributs value"
        return context


class ProductAttributeValueDetailView(DetailView):
    model = ProductAttributeValue
    template_name = "monapp/detail_product_attribute_value.html"
    context_object_name = "product_attribute_value"

    def get_context_data(self, **kwargs):
        context = super(ProductAttributeValueDetailView, self).get_context_data(
            **kwargs
        )
        context["titremenu"] = "Détail de la valeur d'attribut"
        return context


class ProductAttributeValueCreateView(CreateView):
    model = ProductAttributeValue
    form_class = ProductAttributeValueForm
    template_name = "monapp/new_product_attribute_value.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        product_attribute_value = form.save()
        return redirect("product-attribute-value-detail", product_attribute_value.id)


# Ajout du décorateur login_required à une CBV
@method_decorator(login_required, name="dispatch")
class ProductAttributeValueUpdateView(UpdateView):
    model = ProductAttributeValue
    form_class = ProductAttributeValueForm
    template_name = "monapp/update_product_attribute_value.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        product_attribute_value = form.save()
        return redirect("product-attribute-value-detail", product_attribute_value.id)


# Ajout du décorateur login_required à une CBV
@method_decorator(login_required, name="dispatch")
class ProductAttributeValueDeleteView(DeleteView):
    model = ProductAttributeValue
    template_name = "monapp/delete_product_attribute_value.html"
    success_url = reverse_lazy("product-attribute-value-list")


@login_required(login_url="/monapp/login/")
def ContactView(request):
    titreh1 = "Contact us !"
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MonProjet Contact Us form',
                message=form.cleaned_data["message"],
                from_email=form.cleaned_data["email"],
                recipient_list=["cyprientiti37@gmail.com"],
            )
            return redirect("email-sent")
    else:
        form = ContactUsForm()
    return render(request, "monapp/contact.html", {"titreh1": titreh1, "form": form})


def email_sent_view(request):
    return render(request, "monapp/email_sent.html")


class AboutView(TemplateView):
    template_name = "monapp/about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context["titreh1"] = "About us..."
        return context

    def post(self, request, **kwargs):
        return render(request, self.template_name)


class ConnectView(LoginView):
    template_name = "monapp/login.html"

    def post(self, request, **kwargs):
        username = request.POST.get("username", False)
        password = request.POST.get("password", False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return render(
                request,
                "monapp/hello.html",
                {"titreh1": "hello " + username + ", you're connected"},
            )
        else:
            return render(request, "monapp/register.html")


class RegisterView(TemplateView):
    template_name = "monapp/register.html"

    def post(self, request, **kwargs):
        username = request.POST.get("username", False)
        mail = request.POST.get("mail", False)
        password = request.POST.get("password", False)
        user = User.objects.create_user(username, mail, password)
        user.save()
        if user is not None and user.is_active:
            return render(request, "monapp/login.html")
        else:
            return render(request, "monapp/register.html")


class DisconnectView(TemplateView):
    template_name = "monapp/logout.html"

    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name)

def is_admin(user):
    return user.is_superuser

@method_decorator(user_passes_test(is_admin), name="dispatch")
class OrdersView(TemplateView):
    template_name = "monapp/orders.html"

    def post(self, request, **kwargs):
        return render(request, self.template_name)