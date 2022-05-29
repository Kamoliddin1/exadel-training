from django.urls import path

from .views.account import AccountViewSet
from .views.company import CompanyViewSet
from .views.city import CityModelViewSet
from .views.country import CountryViewSet
from .views.user import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'accounts', AccountViewSet, basename='account')
router.register(r'cities', CityModelViewSet, basename='city')
router.register(r'companies', CompanyViewSet, basename='company')
router.register(r'countries', CountryViewSet, basename='country')
router.register(r'users', UserViewSet, basename='user')
urlpatterns = router.urls
