from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter
from . import views

router = DefaultRouter()
router.register('cars', views.Car_list, basename='cars')

urlpatterns = [
    path('cars/', views.Car_list.as_view()),
    path('features/', views.CarFeature_list.as_view()),
    path('customers/', views.Customer_list.as_view())
    # path('', include(router.urls))
]
