from django.db import models
from django.utils import timezone

class FirstDataList(models.Model):
    product_name = models.CharField('Product name', max_length=250)
    description = models.TextField('Description')
    price = models.FloatField('Price', max_length=250)
    status  = models.BooleanField('Status')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "First data list"
        verbose_name_plural = "First data list"

class SecondDataList(models.Model):
    product_name = models.CharField('Product name', max_length=250)
    description = models.TextField('Description')
    price = models.FloatField('Price', max_length=250)
    status  = models.BooleanField('Status')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Second data list"
        verbose_name_plural = "Second data list"


class ThirdDataList(models.Model):
    product_name = models.CharField('Product name', max_length=250)
    description = models.TextField('Description')
    price = models.FloatField('Price', max_length=250)
    status  = models.BooleanField('Status')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Third data list"
        verbose_name_plural = "Third data list"