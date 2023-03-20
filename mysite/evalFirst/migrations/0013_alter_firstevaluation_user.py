# Generated by Django 4.1.7 on 2023-03-20 03:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('evalFirst', '0012_alter_firstevaluation_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstevaluation',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='firstEvaluation', to=settings.AUTH_USER_MODEL),
        ),
    ]
