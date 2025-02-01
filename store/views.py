from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from .models import Car, CarFeature, Customer
from .serializers import CarFeatureSerializer, CarSerializer, CustomerSerializer


# Create your views here.


class CarViewSet(ModelViewSet):

    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CustomerViewSet(ListModelMixin, GenericViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    # @action(
    #     detail=True,
    # )
    # def history(self, request, pk):
    #     return Response("ok")

    # @action(detail=False, methods=["GET", "PUT"])
    # def me(self, request):
    #     customer = Customer.objects.get(user_id=request.user.id)
    #     if request.method == "GET":
    #         serialize = CustomerSerializer(customer)
    #         return Response(serialize.data)
    #     elif request.method == "PUT":
    #         serialize = CustomerSerializer(customer, data=request.data)
    #         serialize.is_valid(raise_exception=True)
    #         serialize.save()
    #         return Response(serialize.data)

    # @action(detail=True, methods=["get"])
    # def custom_action(self, request, pk=None):
    #     # Example custom action logic
    #     return Response({"status": "success"})


class CarFeatureViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarFeatureSerializer

    def get_serializer_context(self):
        return {"request": self.request}
