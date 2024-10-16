from django.db import models
from django.utils import timezone

PRODUCT_STATUS = ((0, "Offline"), (1, "Online"), (2, "Out of stock"))

# Create your models here.
"""
    Status : numero, libelle
"""


class Status(models.Model):
    numero = models.IntegerField()
    libelle = models.CharField(max_length=100)

    def get_libelle(self):
        return self.libelle

    def __str__(self):
        return "{0} {1}".format(self.numero, self.libelle)


"""
Produit : nom, code, etc.
"""


class Product(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, null=True, blank=True, unique=True)
    price_ht = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name="Prix unitaire HT")
    price_ttc = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name="Prix unitaire TTC")
    status = models.SmallIntegerField(choices=PRODUCT_STATUS, default=0)
    date_creation = models.DateTimeField(blank=True, verbose_name="Date création", default=timezone.now)
    stock = models.IntegerField(default=0)
    suppliers = models.ManyToManyField('Supplier', through='ProductSupplier')

    def __str__(self):
        return "{0} {1}".format(self.name, self.code)



"""
    Déclinaison de produit déterminée par des attributs comme la couleur, etc.
"""


class ProductItem(models.Model):

    class Meta:
        verbose_name = "Déclinaison Produit"

    color = models.CharField(max_length=100)
    code = models.CharField(max_length=10, null=True, blank=True, unique=True)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    attributes = models.ManyToManyField(
        "ProductAttributeValue", related_name="product_item", blank=True
    )

    def __str__(self):
        return "{0} {1}".format(self.color, self.code)


class ProductAttribute(models.Model):
    """
    Attributs produit
    """

    class Meta:
        verbose_name = "Attribut"

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductAttributeValue(models.Model):
    """
    Valeurs des attributs
    """

    class Meta:
        verbose_name = "Valeur attribut"
        ordering = ["position"]

    value = models.CharField(max_length=100)
    product_attribute = models.ForeignKey(
        "ProductAttribute", verbose_name="Unité", on_delete=models.CASCADE
    )
    position = models.PositiveSmallIntegerField("Position", null=True, blank=True)

    def __str__(self):
        return "{0} [{1}]".format(self.value, self.product_attribute)

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.TextField()

    def __str__(self):
        return self.name


class ProductSupplier(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        unique_together = ('product', 'supplier')

    def __str__(self):
        return f"{self.product.name} - {self.supplier.name} : {self.price}"

class Order(models.Model):
    STATUS_CHOICES = [
        ('preparation', 'En préparation'),
        ('placed', 'Passée'),
        ('received', 'Reçue'),
    ]
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='preparation')
    date_ordered = models.DateTimeField(default=timezone.now)

    date_received = models.DateTimeField(null=True, blank=True,default=timezone.now)

    def __str__(self):
        return f"Order {self.id} from {self.supplier.name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in order {self.order.id}"
