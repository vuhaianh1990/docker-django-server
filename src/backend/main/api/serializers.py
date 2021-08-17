from rest_framework import serializers
from backend.main.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description',
            'amount', 'created_at', 'updated_at'
        )