# Generated by Django 5.0.2 on 2024-02-16 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='experience',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='skill',
            field=models.IntegerField(default=0),
        ),
    ]
