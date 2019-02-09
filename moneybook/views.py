from django.shortcuts import render, redirect
from django.views import View
from django.utils import timezone
import datetime


from .forms import ExpenditureForm
from .models import ExpenditureDetail

TODAY = str(timezone.now()).split('-')
# Create your views here.
class MainView(View):
    def get(self, request, year=TODAY[0], month=TODAY[1]):
        money = ExpenditureDetail.objects.filter(
            used_date__year=year,
            used_date__month=month
        ).order_by('used_date')

        next_year, next_month = get_next(year, month)
        prev_year, prev_month = get_prev(year, month)

        context = {
            'year' : year,
            'month' : month,
            'next_year' : next_year,
            'next_month' : next_month,
            'prev_year' : prev_year,
            'prev_month' : prev_month,
            'form' : ExpenditureForm()
        }
        return render(request, 'moneybook/mainview.html', context)

    def post(self, request):
        data = request.POST

        used_date = data['used_date']
        cost = data['cost']
        money_use = data['money_use']
        category_choices = data['category']

        used_date = timezone.datetime.strptime(used_date, '%Y-%m-%d')

        ExpenditureDetail.objects.create(
            used_date = used_date,
            cost = cost,
            money_use = money_use,
            category = category_choices
        )

        return redirect(to='/')


def get_next(year, month):
    year = int(year)
    month = int(month)

    if month == 12:
        return str(year + 1), '1'
    else:
        return str(year), str(month + 1)

def get_prev(year, month):
    year = int(year)
    month = int(month)
    if month == 1:
        return str(year - 1), '12'
    else:
        return str(year), str(month - 1)
