from pprint import pprint
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter
from . import views

router = DefaultRouter()
router.register("cars", views.CarViewSet, basename="car")
router.register("customers", views.CustomerViewSet, basename="customer")

urlpatterns = [path("", include(router.urls))]
