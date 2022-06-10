from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views.account import AccountViewSet
from .views.company import CompanyViewSet
from .views.city import CityModelViewSet
from .views.country import CountryViewSet
from .views.user import UserViewSet
from .views.branch import BranchViewSet
from .views.rating import RatingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'accounts', AccountViewSet, basename='account')
router.register(r'cities', CityModelViewSet, basename='city')
router.register(r'companies', CompanyViewSet, basename='company')
router.register(r'countries', CountryViewSet, basename='country')
router.register(r'users', UserViewSet, basename='user')
router.register(r'branches', BranchViewSet, basename='branch')
router.register(r'ratings', RatingViewSet, basename='rating')
router_urls = router.urls
auth_urls = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns = router_urls + auth_urls
