# Generated by Django 3.1 on 2021-01-19 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Uygulama', '0004_auto_20210119_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='todos',
            name='todoname',
            field=models.CharField(blank=True, default=0, max_length=500, verbose_name='Açıklama'),
        ),
    ]
