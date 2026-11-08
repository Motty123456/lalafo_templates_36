from .models import Product
from django.forms import ModelForm

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['product_name','price','category','product_image',
                  'phone_number','descriptions','user','product_type']