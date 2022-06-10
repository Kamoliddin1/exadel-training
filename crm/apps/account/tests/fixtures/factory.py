import factory
from faker import Faker
from apps.account.models import Company, City, Country, Account, User, Branch, Rating
import random

fake = Faker()


class CountryFactory(factory.django.DjangoModelFactory):
    name = fake.country()

    class Meta:
        model = Country


class CityFactory(factory.django.DjangoModelFactory):
    country = factory.SubFactory(CountryFactory)
    name = fake.city()

    class Meta:
        model = City


class AccountCompanyFactory(factory.django.DjangoModelFactory):
    username = fake.company().split()[0]
    is_company = True
    is_user = False

    class Meta:
        model = Account


class AccountClientFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: "bob{}".format(n))
    is_company = False
    is_user = True

    class Meta:
        model = Account


class UserFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(AccountClientFactory)
    house_number = fake.street_address()
    total_area = fake.random_number()
    street = fake.street_name()
    city = factory.SubFactory(CityFactory)

    class Meta:
        model = User


class RatingFactory(factory.django.DjangoModelFactory):
    author = factory.SubFactory(UserFactory)
    rate = random.randint(1, 5)
    review = fake.text()
    timestamp = fake.date_time()

    class Meta:
        model = Rating


class CompanyFactory(factory.django.DjangoModelFactory):
    title = fake.company()
    company = factory.SubFactory(AccountCompanyFactory)
    street = fake.street_name()
    city = factory.SubFactory(CityFactory)

    class Meta:
        model = Company


class BranchFactory(factory.django.DjangoModelFactory):
    name = fake.last_name()
    company = factory.SubFactory(CompanyFactory)

    class Meta:
        model = Branch
