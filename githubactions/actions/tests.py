from django.test import TestCase
from .models import FirstDataList, SecondDataList, ThirdDataList



class FirstDataListTest(TestCase):
    def test_by_existing(self):
        data = FirstDataList.objects.create(
            product_name = 'Book',
            description = 'Rich Papa, poor papa',
            price = '1000',
            status = True,
        )
        self.assertTrue(FirstDataList.objects.filter(product_name = 'Book', description='Rich Papa, poor papa', price = '1000', status = True).exists())


class SecondDataListTest(TestCase):
    def test_by_existing(self):
        data = SecondDataList.objects.create(
            product_name = 'Pen',
            description = 'Speed writer 2000',
            price = '100',
            status = False,
        )
        self.assertTrue(SecondDataList.objects.filter(product_name = 'Pen', description='Speed writer 2000', price = '100', status = False).exists())


class ThirdDataListTest(TestCase):
    def test_by_existing(self):
        data = ThirdDataList.objects.create(
            product_name = 'Water',
            description = '3 liters',
            price = '10',
            status = False,
        )
        self.assertTrue(ThirdDataList.objects.filter(product_name = 'Water', description='3 liters', price = '10', status = False).exists())