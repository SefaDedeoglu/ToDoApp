# Generated by Django 3.1 on 2021-01-20 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Uygulama', '0008_auto_20210120_0105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todos',
            name='a',
        ),
        migrations.RemoveField(
            model_name='todos',
            name='d',
        ),
        migrations.RemoveField(
            model_name='todos',
            name='t',
        ),
        migrations.RemoveField(
            model_name='todos',
            name='y',
        ),
    ]
