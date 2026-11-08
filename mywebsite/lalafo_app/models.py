from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)
    category_image = models.ImageField(upload_to='photo_categoryies')

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.PositiveSmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    product_image = models.ImageField(upload_to='photo_products')
    phone_number = PhoneNumberField(region='KG')
    descriptions = models.TextField()
    user = models.CharField(max_length=54)
    product_type = models.BooleanField(default=False)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.product_name} {self.price}'
