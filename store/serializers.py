from rest_framework import serializers
from store.models import Car, CarFeature, Review, Customer


class CarFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarFeature
        fields = ["id", "car_body", "door", "hp_power", "steering", "traction"]


# class CarSpecsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CarFeature()
#         fields=[]


class CarSerializer(serializers.ModelSerializer):

    car_feature = CarFeatureSerializer(read_only=True)

    class Meta:
        model = Car
        fields = [
            "id",
            "make",
            "model",
            "condition",
            "price",
            "transmission",
            "fuel_type",
            "car_feature",
        ]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["id", "first_name", "email", "phone_number"]


class ReviewSerializer(serializers.ModelSerializer):
    model = Review
    fields = ["id"]

    def create(self, validated_data):
        car_id = self.context["car_id"]
        return Review.objects.create(car_id=car_id, **validated_data)
