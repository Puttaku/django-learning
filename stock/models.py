from django.db import models
class Product (models.Model):

    product_name = models.CharField(max_length=120)
    product_detail = models.TextField("")
    product_barcode = models.CharField(max_length=32)
    product_qty = models.IntegerField()
    product_price = models.DecimalField(max_digits=7, decimal_places=2)
    product_image = models.CharField(max_length=64)
    product_status = models.IntegerField()

