from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class ExpenditureDetail(models.Model):
    category_choices = (
        ('food', '食費'),    # DB値 : 人に読みやすい表示
        ('fare', '交通費'),
        ('medical', '医療費'),
        ('tuition', '学費'),
        ('amusement', '娯楽費'),
        ('tax', '税金'),
        ('communication', '通信費'),
        ('clothes', '衣料品'),
        ('others', '雑費'),
    )

    # データベースの値の項目、1つ1つのデータに対して下の4つの項目が割り当てられる
    used_date = models.DateField()
    cost = models.IntegerField(default=0)
    money_use = models.CharField(max_length=200)
    category = models.CharField(max_length=10, choices=category_choices)

    def __str__(self):
        return self.money_use + ' ￥' + str(self.cost)


class ReceiptImage(models.Model):
    img = models.ImageField(upload_to="receipt")
