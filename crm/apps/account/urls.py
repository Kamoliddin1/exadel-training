from django.urls import path

from .views.city import CityListCreateAPIView, CityRetrieveUpdateDestroyAPIView
from .views.country import country_list, country_detail, CountryListView, CountryDetailView,\
    CountryListCreateAPIView, CountryRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('country', country_list, name='country_list'),
    path('country/<int:pk>', country_detail, name='country_detail'),
    path('country2/', CountryListView.as_view(), name='countries_listview'),
    path('country2/<int:pk>', CountryDetailView.as_view(), name='countries_detailview'),
    path('country3/', CountryListCreateAPIView.as_view(), name='countries_list_apiview'),
    path('country3/<int:pk>', CountryRetrieveUpdateDestroyAPIView.as_view(), name='countries_list_apiview'),

    path('city/', CityListCreateAPIView.as_view()),
    path('city/<int:pk>/', CityRetrieveUpdateDestroyAPIView.as_view())
]
