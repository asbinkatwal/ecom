from django.db import models
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
    Title = models.CharField(_("Title"), max_length=50)
    Price= models.FloatField(_("Price"))
    Description= models.TextField(_("Description"))
    Category= models.CharField(_("Category"), max_length=50)
    Image= models.FileField(_("Image"), upload_to='Product_image/', max_length=100)



    def __str__(self):
        return self.Title




    
