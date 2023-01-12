# Generated by Django 4.1.3 on 2023-01-09 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evalFirst', '0002_firstevaluation_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstevaluation',
            name='student_id',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='firstQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question1', models.IntegerField(choices=[(3, 'Exceeds Expectations'), (2, 'Meets Expectations'), (1, 'Emerging'), (0, 'Does Not Meet Expectations')], default=0)),
                ('question2', models.IntegerField(choices=[(3, 'Exceeds Expectations'), (2, 'Meets Expectations'), (1, 'Emerging'), (0, 'Does Not Meet Expectations')], default=0)),
                ('question3', models.IntegerField(choices=[(3, 'Exceeds Expectations'), (2, 'Meets Expectations'), (1, 'Emerging'), (0, 'Does Not Meet Expectations')], default=0)),
                ('question4', models.IntegerField(choices=[(3, 'Exceeds Expectations'), (2, 'Meets Expectations'), (1, 'Emerging'), (0, 'Does Not Meet Expectations')], default=0)),
                ('question5', models.IntegerField(choices=[(3, 'Exceeds Expectations'), (2, 'Meets Expectations'), (1, 'Emerging'), (0, 'Does Not Meet Expectations')], default=0)),
                ('question6', models.IntegerField(choices=[(3, 'Exceeds Expectations'), (2, 'Meets Expectations'), (1, 'Emerging'), (0, 'Does Not Meet Expectations')], default=0)),
                ('question7', models.IntegerField(choices=[(3, 'Exceeds Expectations'), (2, 'Meets Expectations'), (1, 'Emerging'), (0, 'Does Not Meet Expectations')], default=0)),
                ('question8', models.IntegerField(choices=[(3, 'Exceeds Expectations'), (2, 'Meets Expectations'), (1, 'Emerging'), (0, 'Does Not Meet Expectations')], default=0)),
                ('question9', models.IntegerField(choices=[(3, 'Exceeds Expectations'), (2, 'Meets Expectations'), (1, 'Emerging'), (0, 'Does Not Meet Expectations')], default=0)),
                ('question10', models.IntegerField(choices=[(3, 'Exceeds Expectations'), (2, 'Meets Expectations'), (1, 'Emerging'), (0, 'Does Not Meet Expectations')], default=0)),
                ('question11', models.IntegerField(choices=[(3, 'Exceeds Expectations'), (2, 'Meets Expectations'), (1, 'Emerging'), (0, 'Does Not Meet Expectations')], default=0)),
                ('question12', models.IntegerField(choices=[(3, 'Exceeds Expectations'), (2, 'Meets Expectations'), (1, 'Emerging'), (0, 'Does Not Meet Expectations')], default=0)),
                ('question13', models.IntegerField(choices=[(3, 'Exceeds Expectations'), (2, 'Meets Expectations'), (1, 'Emerging'), (0, 'Does Not Meet Expectations')], default=0)),
                ('question14', models.IntegerField(choices=[(3, 'Exceeds Expectations'), (2, 'Meets Expectations'), (1, 'Emerging'), (0, 'Does Not Meet Expectations')], default=0)),
                ('question15', models.IntegerField(choices=[(3, 'Exceeds Expectations'), (2, 'Meets Expectations'), (1, 'Emerging'), (0, 'Does Not Meet Expectations')], default=0)),
                ('question16', models.IntegerField(choices=[(3, 'Exceeds Expectations'), (2, 'Meets Expectations'), (1, 'Emerging'), (0, 'Does Not Meet Expectations')], default=0)),
                ('question17', models.IntegerField(choices=[(3, 'Exceeds Expectations'), (2, 'Meets Expectations'), (1, 'Emerging'), (0, 'Does Not Meet Expectations')], default=0)),
                ('question18', models.IntegerField(choices=[(3, 'Exceeds Expectations'), (2, 'Meets Expectations'), (1, 'Emerging'), (0, 'Does Not Meet Expectations')], default=0)),
                ('question19', models.IntegerField(choices=[(3, 'Exceeds Expectations'), (2, 'Meets Expectations'), (1, 'Emerging'), (0, 'Does Not Meet Expectations')], default=0)),
                ('question20', models.IntegerField(choices=[(3, 'Exceeds Expectations'), (2, 'Meets Expectations'), (1, 'Emerging'), (0, 'Does Not Meet Expectations')], default=0)),
                ('question21', models.IntegerField(choices=[(3, 'Exceeds Expectations'), (2, 'Meets Expectations'), (1, 'Emerging'), (0, 'Does Not Meet Expectations')], default=0)),
                ('comment', models.CharField(max_length=1000)),
                ('firstEvaluation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evalFirst.firstevaluation')),
            ],
        ),
    ]