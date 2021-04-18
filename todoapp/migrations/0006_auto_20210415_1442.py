# Generated by Django 3.1.7 on 2021-04-15 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0005_auto_20210415_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.IntegerField(choices=[('A', 'Высокий'), ('B', 'Средний'), ('C', 'Низкий')], default=0, null=True),
        ),
    ]
