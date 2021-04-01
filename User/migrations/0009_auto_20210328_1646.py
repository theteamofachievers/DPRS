# Generated by Django 3.1.1 on 2021-03-28 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0008_admission'),
    ]

    operations = [
        migrations.AddField(
            model_name='admission',
            name='bill',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='admission',
            name='billpaid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='admission',
            name='cause',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='admission',
            name='expense',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='admission',
            name='prescription',
            field=models.CharField(default='', max_length=2250),
        ),
        migrations.AddField(
            model_name='admission',
            name='report',
            field=models.CharField(default='', max_length=250),
        ),
    ]