from pytest_factoryboy import register
from fixtures.factory import (AccountCompanyFactory, AccountClientFactory,
                              CountryFactory, CityFactory, CompanyFactory,
                              UserFactory)

register(AccountClientFactory)
register(AccountCompanyFactory)
register(CountryFactory)
register(CityFactory)
register(CompanyFactory)
register(UserFactory)
