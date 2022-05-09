from django.urls import path
from .views import (index, BranchListView, CompanyListView,
                    UserListView, CompanyCreateView)

urlpatterns = [
    path('', index, name='index'),
    path('branches', BranchListView.as_view(), name='branches'),
    path('companies', CompanyListView.as_view(), name='companies'),
    path('users', UserListView.as_view(), name='users'),
    path('create', CompanyCreateView.as_view(), name="create"),
]
