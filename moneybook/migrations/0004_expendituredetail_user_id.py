# Generated by Django 2.1.7 on 2019-07-07 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moneybook', '0003_auto_20190303_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='expendituredetail',
            name='user_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]