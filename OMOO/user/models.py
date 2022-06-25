from hmac import digest
from string import digits
from unicodedata import digit
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# from address.models import AddressField
from phonenumber_field.modelfields import PhoneNumberField

from .managers import CustomUserManager


class ModelStateFieldsCacheDescriptor:
    def __get__(self, instance, cls=None):
        if instance is None:
            return self
        res = instance.fields_cache = {}
        return res


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_("first name"), max_length=50)
    last_name = models.CharField(_("last name"), max_length=50)
    username = models.CharField(_("user name"), unique=True, max_length=50)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_inventory_manager = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "email",
    ]

    objects = CustomUserManager()

    class Meta:
        app_label = "user"
        db_table = ""
        managed = True
        verbose_name = "system user"
        verbose_name_plural = "system users"
        order_with_respect_to = "is_staff"

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"



class Customer(CustomUser):
    phone = PhoneNumberField(null=True, blank=True, unique=False)
    address = models.TextField(default=None, blank=True, max_length=255)

    class Meta:
        db_table = ""
        managed = True
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return str(self.person_name)


class Rider(CustomUser):
    cnic = models.PositiveIntegerField(default=3820108024211)
    phone = PhoneNumberField(null=True, blank=True, unique=False)
    address = models.TextField(default=None, blank=True, max_length=255)

    class Meta:
        db_table = ""
        managed = True
        verbose_name = "Rider"
        verbose_name_plural = "Riders"

    def __str__(self):
        return str(self.person_name)