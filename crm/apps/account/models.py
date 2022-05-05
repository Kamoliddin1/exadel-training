from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from django.db import models
from django.conf import settings


class Country(models.Model):
    name = models.CharField(max_length=100)


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)


class Address(models.Model):
    street = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True


class Company(Address):
    title = models.CharField(max_length=200)
    company = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                   primary_key=True, related_name='companies')


class Branch(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='branches')


class Account(AbstractUser):
    is_user = models.BooleanField()
    is_company = models.BooleanField()


class User(Address):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True, related_name='users')
    house_number = models.CharField(max_length=50)
    total_area = models.FloatField()

    def __str__(self):
        return self.user.first_name


class Rating(models.Model):
    rate_choices = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rate = models.IntegerField(choices=rate_choices)
    review = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
