# Generated by Django 3.1 on 2021-01-19 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Uygulama', '0007_auto_20210120_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='a',
            field=models.CharField(blank=True, default=0, max_length=2, verbose_name='a'),
        ),
        migrations.AlterField(
            model_name='todos',
            name='d',
            field=models.CharField(blank=True, default=0, max_length=2, verbose_name='d'),
        ),
        migrations.AlterField(
            model_name='todos',
            name='y',
            field=models.CharField(blank=True, default=0, max_length=2, verbose_name='y'),
        ),
    ]
