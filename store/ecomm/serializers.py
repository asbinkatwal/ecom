from rest_framework import serializers
from.models import product

class productsearilizer(serializers.ModelSerializer):
    class Meta:
        
        models = product
        fields =' __all__'