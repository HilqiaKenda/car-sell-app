from django.db import models


# Create your models here.


class CarFeature(models.Model):
    TRACTION_FWD = "F"
    TRACTION_RWD = "R"
    TRACTION_4WD = "4"
    TRACTION_AWD = "A"

    STEERING_LEFT = "L"
    STEERING_RIGHT = "R"

    TRACTION_CHOICES = [
        (TRACTION_FWD, "FWD"),
        (TRACTION_RWD, "RWD"),
        (TRACTION_4WD, "4WD"),
        (TRACTION_AWD, "AWD"),
    ]

    STEERING_CHOICES = [(STEERING_LEFT, "Left"), (STEERING_RIGHT, "Right")]

    car_body = models.CharField(max_length=50)
    hp_power = models.CharField(max_length=50)
    door = models.CharField(max_length=10)
    traction = models.CharField(max_length=5, choices=TRACTION_CHOICES)
    steering = models.CharField(
        max_length=5, choices=STEERING_CHOICES, default=STEERING_LEFT
    )


class Car(models.Model):
    CONDITION_USED = "U"
    CONDITION_BRAND_NEW = "N"

    FUEL_TYPE_PETROL = "P"
    FUEL_TYPE_FUEL = "F"
    FUEL_TYPE_ELECTRIC = "E"
    FUEL_TYPE_HYBRID = "H"

    TRANSMISSION_MANUAL = "M"
    TRANSMISSION_SEQUENTIAL = "S"
    TRANSMISSION_SEMI_AUTO = "S"
    TRANSMISSION_AUTO = "A"
    TRANSMISSION_DCT = "T"

    CONDITION_CHOICES = [(CONDITION_USED, "Used"), (CONDITION_BRAND_NEW, "Brand New")]
    FUEL_TYPE_CHOICES = [
        (FUEL_TYPE_PETROL, "Petrol"),
        (FUEL_TYPE_FUEL, "Fuel"),
        (FUEL_TYPE_ELECTRIC, "Electric"),
        (FUEL_TYPE_HYBRID, "Hybrid"),
    ]

    TRANSMISSION_CHOICES = [
        (TRANSMISSION_AUTO, "Automatic"),
        (TRANSMISSION_SEMI_AUTO, "Semi Automatic"),
        (TRANSMISSION_MANUAL, "Manual"),
        (TRANSMISSION_SEQUENTIAL, "Sequential"),
    ]

    make = models.CharField(max_length=255)
    model = models.CharField(max_length=50)
    year = models.DateField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    color = models.CharField(max_length=50)
    condition = models.CharField(
        max_length=50, choices=CONDITION_CHOICES, default=CONDITION_USED
    )
    transmission = models.CharField(
        max_length=20, choices=TRANSMISSION_CHOICES, default=TRANSMISSION_AUTO
    )
    fuel_type = models.CharField(
        max_length=10, choices=FUEL_TYPE_CHOICES, default=FUEL_TYPE_PETROL
    )
    description = models.TextField()
    mileage = models.CharField(max_length=255)
    car_feature = models.ForeignKey(
        CarFeature, on_delete=models.CASCADE, default=None, related_name="feature"
    )


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=20, null=True)
    birth_date = models.DateField(null=True)
    car = models.ManyToManyField(Car)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)


class Order(models.Model):
    payment_pending = "p"
    payment_complete = "C"
    payment_failed = "F"
    PAYMENT_STATUS_CHOICES = [
        (payment_pending, "pending"),
        (payment_complete, "complete"),
        (payment_failed, "failed"),
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=payment_pending
    )
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
