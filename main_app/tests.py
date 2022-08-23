from django.test import TestCase
from .models import Invoice


class InvoiceTestCase(TestCase):
    def setUp(self) -> None:
        Invoice.objects.create(name='testing')

    def test_full_price(self):
        invoice = Invoice.objects.get(name='testing')
        self.assertEqual(invoice.full_price, 0)
