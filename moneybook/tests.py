from django.test import TestCase
from django.utils import timezone
from django.urls import resolve

from moneybook.models import ExpenditureDetail
from moneybook.views import MainView

# Create your tests here.
class TestExpenditureDetail(TestCase):
    def setUp(self):
        used_date = timezone.now()
        money_use = 'おにぎり'
        cost = 100
        category = 'food'

        ExpenditureDetail.objects.create(
            used_date = used_date,
            money_use = money_use,
            cost = cost,
            category = category,
        )

    def test_save_data(self):
        onigiri = ExpenditureDetail.objects.all()
        self.assertEqual(onigiri.count(), 1)
        self.assertEqual(onigiri[0].used_date, timezone.localdate())
        self.assertEqual(onigiri[0].money_use, 'おにぎり')
        self.assertEqual(onigiri[0].cost, 100)
        self.assertEqual(onigiri[0].category, 'food')

        return None

    def test_update_data(self):
        onigiri = ExpenditureDetail.objects.filter(cost = 100).update(category = 'tax')
        onigiri = ExpenditureDetail.objects.all()
        self.assertEqual(onigiri[0].category, 'tax')

        return None

    def test_delete_data(self):
        onigiri = ExpenditureDetail.objects.all().delete()
        onigiri = ExpenditureDetail.objects.all()
        self.assertEqual(onigiri.count(), 0)

        return None



class TestURL(TestCase):
    def test_url_resolve(self):
        url = resolve('/')
        self.assertEqual(url.func.view_class, MainView)
