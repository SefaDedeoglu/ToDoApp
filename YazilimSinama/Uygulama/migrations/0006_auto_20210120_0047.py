# Generated by Django 3.1 on 2021-01-19 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Uygulama', '0005_todos_todoname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='todoname',
            field=models.CharField(blank=True, default=0, max_length=500, verbose_name='todoName'),
        ),
    ]
