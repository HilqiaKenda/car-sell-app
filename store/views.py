from rest_framework.views import APIView
from .models import Car, CarFeature, customer
from .serializers import CarFeatureSerializer, CarSerializer, CustomerSerializer


# Create your views here.

class Car_list(APIView):
    
    def get_queryset(self):
        return Car.objects.all()
    
    def get_serializer_class(self):
        return CarSerializer

class Customer_list(APIView):
    def get_queryset(self):
        return customer.objects.all()
    
    def get_serialiazer_class(self):
        return CustomerSerializer

class CarFeature_list(APIView):
    def get_queryset(self):
        return CarFeature.objects.all()
    
    def get_serializer_class(self):
        return CarFeatureSerializer
    