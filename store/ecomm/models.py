from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Product(models.Model):
    Title = models.CharField(_("Title"), max_length=50)
    Price= models.FloatField(_("Price"))
    Description= models.TextField(_("Description"))
    Category= models.CharField(_("Category"), max_length=50)
    Image= models.FileField(_("Image"), upload_to='Product_image/', max_length=100)



    def __str__(self):
        return self.Title

class CartItem(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} x{self.quantity}"


    
