# Generated by Django 3.1.1 on 2021-03-28 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0011_admission_admitdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='admission',
            name='dischargeDate',
            field=models.CharField(default='', max_length=100),
        ),
    ]