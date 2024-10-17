from django.test import TestCase
from monapp.models import Order, Product, OrderItem,Supplier

class OrderModelTest(TestCase):
    
    def setUp(self):
        self.supplier = Supplier.objects.create(name="Fournisseur 1",
        contact_info="0248550591")
        self.order = Order.objects.create(date_ordered="2022-01-01", date_received="2022-01-02",status="preparation", supplier_id=self.supplier.id)
        self.product = Product.objects.create(name="Produit 1", code=10,status=1,date_creation="2022-01-01", price_ht=10.00, price_ttc=12.00, stock=220)
        self.order_item = OrderItem.objects.create(order_id=self.order.id, product_id=self.product.id, quantity=5)
    
    def test_order_creation(self):
        
        self.assertEqual(self.order.date_ordered, "2022-01-01")
        self.assertEqual(self.order.date_received, "2022-01-02")
        self.assertEqual(self.order.status, "preparation")
        self.assertEqual(self.order_item.order_id, self.order.id)
        self.assertEqual(self.order.supplier_id, self.supplier.id)
        self.assertEqual(self.order_item.product_id, self.product.id)
        
    
        
    
    def test_update_order(self):
        
        self.order.date_ordered = "2022-01-03"
        self.order.date_received = "2022-01-04"
        self.order.status = "en cours de livraison"
        self.order.save()
        
        self.assertEqual(self.order.date_ordered, "2022-01-03")
        self.assertEqual(self.order.date_received, "2022-01-04")
        self.assertEqual(self.order.status, "en cours de livraison")
        
    def test_add_order_item(self):
        
        new_product = Product.objects.create(name="Produit 2", code=11, status=1, date_creation="2022-01-01", price_ht=15.00, price_ttc=18.00, stock=180)
        new_order_item = OrderItem.objects.create(order_id=self.order.id, product_id=new_product.id, quantity=3)
        self.assertEqual(new_order_item.order_id, self.order.id)
        self.assertEqual(new_order_item.product_id, new_product.id)
        
        
    def test_delete_order(self):
        
        self.order.delete()
        self.assertEqual(Order.objects.count(), 0)
        
    
        
        
    
        
    