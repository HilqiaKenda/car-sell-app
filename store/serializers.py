from rest_framework import serializers
from store.models import Car, CarFeature, Review, customer


class CarFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarFeature
        fields = ["id", "hp_power", "doors", "steering", "traction"]


class CarSerializer(serializers.ModelSerializer):
    specs = CarFeatureSerializer(read_only=True, many=True)

    class Meta:
        model = Car
        fields = [
            "id",
            "model",
            "condition",
            "price",
            "transmission",
            "fuel_type",
            "specs",
        ]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = ["id", "first_name", "email", "phone"]


class ReviewSerializer(serializers.ModelSerializer):
    model = Review
    fields = ["id"]

    def create(self, validated_data):
        car_id = self.context["car_id"]
        return Review.objects.create(car_id=car_id, **validated_data)
