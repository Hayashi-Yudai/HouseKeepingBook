from django.shortcuts import render, redirect
from django.views import View
from django.utils import timezone
import datetime
import calendar


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

        total = 0
        for m in money:
            total += m.cost

        next_year, next_month = get_next(year, month)
        prev_year, prev_month = get_prev(year, month)

        context = {
            'year' : year,
            'month' : month,
            'next_year' : next_year,
            'next_month' : next_month,
            'prev_year' : prev_year,
            'prev_month' : prev_month,
            'total_cost' : total,
            'money' : money,
            'form' : ExpenditureForm()
        }

        self.draw_graph(year, month)

        return render(request, 'moneybook/mainview.html', context)

    def post(self, request, year=TODAY[0], month=TODAY[1]):
        data = request.POST
        form = ExpenditureForm(data)

        if 'add' in data.keys() and form.is_valid():
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

        elif 'delete' in data.keys():
            used_date = data['used_date']
            cost = data['cost']
            money_use = data['money_use']


            used_date = used_date.replace('年', '-').replace('月', '-').replace('日', '')
            y, m, d = used_date.split('-')

            ExpenditureDetail.objects.filter(
                used_date__year=y,
                used_date__month=m,
                used_date__day=d,
                cost__iexact=cost,
                money_use__iexact=money_use
            ).delete()

            return redirect(to=f'/{year}/{month}')

        money = ExpenditureDetail.objects.filter(
            used_date__year=year,
            used_date__month=month
        ).order_by('used_date')

        total = 0
        for m in money:
            total += m.cost

        next_year, next_month = get_next(year, month)
        prev_year, prev_month = get_prev(year, month)

        context = {
            'year' : year,
            'month' : month,
            'next_year' : next_year,
            'next_month' : next_month,
            'prev_year' : prev_year,
            'prev_month' : prev_month,
            'total_cost' : total,
            'money' : money,
            'form' : form,
        }

        self.draw_graph(year, month)

        return render(request, 'moneybook/mainview.html', context)
        #return redirect(to=f'/{year}/{month}')

    def draw_graph(self, year, month):
        money = ExpenditureDetail.objects.filter(used_date__year=year,
                used_date__month=month).order_by('used_date')

        last_day = calendar.monthrange(int(year), int(month))[1] + 1
        day = [i for i in range(1, last_day)]
        cost = [0 for i in range(len(day))]
        for m in money:
            cost[int(str(m.used_date).split('-')[2])-1] += int(m.cost)

        text_day = ','.join(list(map(str, day)))
        text_cost = ','.join(list(map(str, cost)))

        json_template = """var json = {
            type: 'bar',
            data: {
                labels: [
        """ + str(text_day) + """
                ],
                datasets: [{
                    label: '支出',
                    data: [
        """ + str(text_cost) + """
                    ],
                    borderWidth: 2,
                    strokeColor: 'rgba(0,0,255,1)',
                    backgroundColor: 'rgba(0,191,255,0.5)'
                }]
            },
            options: {
                scales: {
                    xAxes: [{
                        ticks: {
                            beginAtZero:true
                        },
                        scaleLabel: {
                            display: true,
                            labelString: '日付',
                            fontsize: 18
                        }
                    }],
                    yAxes: [{
                        ticks: {
                            beginAtZero:true
                        },
                        scaleLabel: {
                            display: true,
                            labelString: '支出額 (円)',
                            fontsize: 18
                        }
                    }]
                },
                responsive: true
            }
        }
        """
        with open('moneybook/static/moneybook/js/data.js', 'w') as f:
            f.write(json_template)



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
