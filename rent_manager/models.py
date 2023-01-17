from django.db import models

# Create your models here.
class Entity(models.Model):
    TYPE_CHOICE=(
        (0, '1RK'),
        (1, '1BHK'),
        (2, 'Shop'),
    )
    type = models.IntegerField(default=0, choices=TYPE_CHOICE)
    number = models.IntegerField(default=0)
    details = models.TextField(blank=True)
    area = models.FloatField(default=0.0)
    rent = models.FloatField(default=0.0)
    deposit = models.FloatField(default=0.0)
    amenities = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=0)
    is_available = models.BooleanField(default=False)


class MaintenanceHistory(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    details = models.TextField(blank=True)
    date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=0)


class TenantProfile(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=15)
    alternate_phone = models.CharField(max_length=15, null=True, blank=True)
    code = models.CharField(max_length=10)
    pan_card = models.ImageField()
    aadhaar_card = models.ImageField()
    photo = models.ImageField()
    village_address = models.TextField(max_length=1000)
    work_address = models.TextField(max_length=1000)
    pdf = models.FileField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=0)


class Tenant(models.Model):
    tenant = models.ForeignKey(TenantProfile, null=True, on_delete=models.SET_NULL)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    rent_amount = models.IntegerField(default=0)
    deposit_amount = models.IntegerField(default=0)
    agreement_start = models.DateField(null=True, blank=True)
    agreement_end = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=0)


class TenantPayment(models.Model):
    tenant = models.ForeignKey(TenantProfile, on_delete=models.CASCADE)
    date = models.DateField()
    amount_due = models.FloatField(default=0.0)
    paid = models.FloatField(default=0.0)
    balance = models.FloatField(default=0.0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=0)