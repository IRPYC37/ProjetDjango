from django.test import TestCase
from monapp.models import Supplier

class SupplierModelTest(TestCase):
    def setUp(self):
        # Créer un fournisseur à utiliser dans les tests
        self.supplier = Supplier.objects.create(name="Fournisseur 1",
        contact_info="0248550591")
        
    def test_supplier_creation(self):
        """
        Tester si un fournisseur est bien créé
        """
        self.assertEqual(self.supplier.name, "Fournisseur 1")
        self.assertEqual(self.supplier.contact_info, "0248550591")
    
    def test_string_representation(self):
        """
        Tester la méthode __str__ du modèle Supplier
        """
        self.assertEqual(str(self.supplier), "Fournisseur 1")
        
    
    def test_update_supplier(self):
        """
        Tester la mise à jour d'un fournisseur
        """
        self.supplier.name = "Fournisseur 2"
        self.supplier.contact_info = "0619042022"
        self.supplier.save()
        # Récupérer l'objet mis à jour
        updated_supplier = Supplier.objects.get(id=self.supplier.id)
        self.assertEqual(updated_supplier.name, "Fournisseur 2")
        self.assertEqual(updated_supplier.contact_info, "0619042022")
        
    def test_delete_supplier(self):
        """
        Tester la suppression d'un fournisseur
        """
        self.supplier.delete()
        self.assertEqual(Supplier.objects.count(), 0)
        
    