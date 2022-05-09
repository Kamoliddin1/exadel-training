from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, View, CreateView

from .models import Company, Branch, User, City, Account


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


class CompanyCreateView(CreateView):
    model = Company
    fields = ['title', 'company', 'city', 'street']

    def post(self, request, *args, **kwargs):
        title = request.POST['title']
        company = request.POST['company']
        city = request.POST['city']
        street = request.POST['street']
        try:
            city_ins = get_object_or_404(City, id=city)
        except City.DoesNotExist:
            city_ins = 1
        try:
            company_ins = get_object_or_404(Account, id=company)
        except City.DoesNotExist:
            company_ins = 1
        obj = Company.objects.create(title=title, company=company_ins, city=city_ins, street=street)

        obj.save()
        return redirect('companies')
