from django.contrib import admin
from .models import (
    City, Country, User,
    Company, Branch, Rating, Account
)

admin.site.register(City)
admin.site.register(Country)
admin.site.register(User)
admin.site.register(Company)
admin.site.register(Branch)
admin.site.register(Rating)
admin.site.register(Account)
