# Generated by Django 4.1.7 on 2023-03-27 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evalFirst', '0016_firstevaluation_evaluationnum'),
    ]

    operations = [
        migrations.AddField(
            model_name='firstevaluation',
            name='date',
            field=models.DateField(default='2023-01-01'),
        ),
    ]