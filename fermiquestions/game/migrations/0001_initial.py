# Generated by Django 5.0.2 on 2024-02-18 23:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('data', '0007_alter_question_options_question_date_made'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_score', models.IntegerField()),
                ('previous_question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.question')),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.repository')),
            ],
        ),
    ]