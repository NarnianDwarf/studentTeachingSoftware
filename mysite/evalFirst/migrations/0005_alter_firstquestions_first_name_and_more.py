# Generated by Django 4.1.3 on 2023-01-30 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evalFirst', '0004_remove_firstquestions_firstevaluation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstquestions',
            name='first_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='firstquestions',
            name='last_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]