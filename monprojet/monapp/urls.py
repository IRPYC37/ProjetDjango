from django.urls import path
from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path('about/', AboutView.as_view(), name='about'),
    path("products/", ProductListView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("product-items/", ProductItemListView.as_view(), name="product-item-list"),
    path(
        "product-items/<int:pk>/",
        ProductItemDetailView.as_view(),
        name="product-item-detail",
    ),
    path(
        "product-attributes/",
        ProductAttributeListView.as_view(),
        name="product-attribute-list",
    ),
    path(
        "product-attributes/<int:pk>/",
        ProductAttributeDetailView.as_view(),
        name="product-attribute-detail",
    ),
    path("login/", ConnectView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", DisconnectView.as_view(), name="logout"),
    path("contact/", ContactView, name="contact"),
    path("email-sent/", email_sent_view, name="email-sent"),
    path("product/add/", ProductCreateView.as_view(), name="product-add"),
    path("product/<pk>/update/", ProductUpdateView.as_view(), name="product-update"),
    path("product/<pk>/delete/", ProductDeleteView.as_view(), name="product-delete"),
    path(
        "product-items/add/", ProductItemCreateView.as_view(), name="product-item-add"
    ),
    path(
        "product-items/<pk>/update/",
        ProductItemUpdateView.as_view(),
        name="product-item-update",
    ),
    path(
        "product-items/<pk>/delete/",
        ProductItemDeleteView.as_view(),
        name="product-item-delete",
    ),
    path(
        "product-attribute/add/",
        ProductAttributeCreateView.as_view(),
        name="product-attribute-add",
    ),
    path(
        "product-attribute/<pk>/update/",
        ProductAttributeUpdateView.as_view(),
        name="product-attribute-update",
    ),
    path(
        "product-attribute/<pk>/delete/",
        ProductAttributeDeleteView.as_view(),
        name="product-attribute-delete",
    ),
    path(
        "product-attributes-value/",
        ProductAttributeValueVListView.as_view(),
        name="product-attribute-value-list",
    ),
    path(
        "product-attribute-value/add/",
        ProductAttributeValueCreateView.as_view(),
        name="product-attribute-value-add",
    ),
        path('product-attribute-value/<pk>/', ProductAttributeValueDetailView.as_view(), name='product-attribute-value-detail'),
    path(
        "product-attribute-value/<pk>/update/",
        ProductAttributeValueUpdateView.as_view(),
        name="product-attribute-value-update",
    ),
    path(
        "product-attribute-value/<pk>/delete/",
        ProductAttributeValueDeleteView.as_view(),
        name="product-attribute-value-delete",
    ),
    path(
        "orders/",
        OrdersView.as_view(),
        name="orders",
    ),
]
