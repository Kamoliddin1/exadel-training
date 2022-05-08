from django.shortcuts import render
from django.views.generic import ListView, View

from .models import Company, Branch, User, City


def index(request):
    context = {'index': 'Hello there'}
    return render(request, 'base.html', context)


class BranchListView(ListView):
    model = Branch
    queryset = Branch.objects.all()


class UserListView(ListView):
    model = User
    queryset = User.objects.filter(user__is_user=True)


class CompanyListView(ListView):
    model = Company
    queryset = Company.objects.filter(company__is_company=True)
