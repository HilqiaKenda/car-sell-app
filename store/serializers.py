from rest_framework import serializers
from store.models import Car, CarFeature, customer


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'model', 'condition','transmission']
        
class CarFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarFeature
        fields = ['id', 'hp_power', 'doors', 'steering','traction']
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = ['id', 'first_name', 'email', 'phone']