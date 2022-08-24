from dataclasses import fields
from rest_framework import serializers
from store.models import Product , OrderItem , Order 
from django.contrib.auth.models import User


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'



