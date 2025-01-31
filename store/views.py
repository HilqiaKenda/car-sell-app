from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from .models import Car, CarFeature, customer
from .serializers import CarFeatureSerializer, CarSerializer, CustomerSerializer


# Create your views here.


class CarList(RetrieveUpdateDestroyAPIView, GenericAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def destroy(self, request, pk):
        car = get_object_or_404(Car, pk=pk)

        if car.pk != pk:
            return Response({"error": "can't be deleted"})
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerList(ListModelMixin):
    quesryset = customer.objects.all()
    serializer_class = CustomerSerializer


class CarFeatureList(ListModelMixin):
    queryset = Car.objects.all()
    serializer_class = CarFeatureSerializer
