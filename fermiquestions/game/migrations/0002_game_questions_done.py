# Generated by Django 5.0.2 on 2024-02-19 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='questions_done',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
