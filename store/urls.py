from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter
from . import views

router = DefaultRouter()
router.register('cars', views.CarList, basename='cars')

urlpatterns = [
    path('cars/<int:pk>', views.CarList.as_view()),
    path('features/', views.CarFeatureList),
    path('customers/', views.CustomerList),
]
