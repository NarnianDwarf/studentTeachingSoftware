# Generated by Django 4.1.7 on 2023-03-27 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evalFirst', '0019_rename_question1a_firstevaluation_pedagogy_a_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='firstevaluation',
            old_name='question5a',
            new_name='Disposition_A',
        ),
        migrations.RenameField(
            model_name='firstevaluation',
            old_name='question5b',
            new_name='Disposition_B',
        ),
        migrations.RenameField(
            model_name='firstevaluation',
            old_name='question5c',
            new_name='Disposition_C',
        ),
        migrations.RenameField(
            model_name='firstevaluation',
            old_name='question5d',
            new_name='Disposition_D',
        ),
        migrations.RenameField(
            model_name='firstevaluation',
            old_name='question5e',
            new_name='Disposition_E',
        ),
        migrations.RenameField(
            model_name='firstevaluation',
            old_name='question6f',
            new_name='Disposition_F',
        ),
        migrations.RenameField(
            model_name='firstevaluation',
            old_name='question6g',
            new_name='Disposition_G',
        ),
        migrations.RenameField(
            model_name='firstevaluation',
            old_name='question7h',
            new_name='Disposition_H',
        ),
    ]