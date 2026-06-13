from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('User', 'User'),
        ('Collector', 'Collector'),
        ('Admin', 'Admin'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='User')

    def __str__(self):
        return self.user.username


class ScrapMaterial(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class PickupRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Assigned', 'Assigned'),
        ('Collected', 'Collected'),
        ('Rejected', 'Rejected'),
        ('Completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    scrap_material = models.ForeignKey(ScrapMaterial, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    pickup_address = models.TextField()
    preferred_date = models.DateField()
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    collector = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_pickups'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request {self.id} - {self.user.username}"


class ScrapCollection(models.Model):
    COLLECTION_STATUS = [
        ('Assigned', 'Assigned'),
        ('Picked Up', 'Picked Up'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
    ]

    pickup_request = models.OneToOneField(PickupRequest, on_delete=models.CASCADE)
    collector = models.ForeignKey(User, on_delete=models.CASCADE)
    actual_weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    collection_date = models.DateField(null=True, blank=True)
    remarks = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=COLLECTION_STATUS, default='Assigned')

    def __str__(self):
        return f"Collection {self.id}"


class Transaction(models.Model):
    PAYMENT_STATUS = [
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
    ]

    pickup_request = models.OneToOneField(PickupRequest, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='Pending')
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.id}"


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message[:40]