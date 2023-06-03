from rest_framework import serializers
from api.order.models import Order



class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['user']
        #TODO: add product and quantity
    
