# Generated by Django 3.1 on 2021-01-19 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Uygulama', '0002_auto_20210119_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joblist',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='joblist',
            name='text',
        ),
        migrations.RemoveField(
            model_name='joblist',
            name='title',
        ),
        migrations.RemoveField(
            model_name='todos',
            name='Todostext',
        ),
        migrations.AddField(
            model_name='joblist',
            name='GerceklesenSure',
            field=models.CharField(default=0, max_length=500, verbose_name='Gerçekleşen Süre'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='joblist',
            name='IsAciklamasi',
            field=models.CharField(default=0, max_length=500, verbose_name='İş Açıklaması'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='joblist',
            name='KartNo',
            field=models.CharField(default=0, max_length=500, verbose_name='Kart No'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='joblist',
            name='Notlar',
            field=models.CharField(default=0, max_length=500, verbose_name='Notlar'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='joblist',
            name='ProjeNo',
            field=models.CharField(default=0, max_length=500, verbose_name='Proje No'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='joblist',
            name='TahminiSure',
            field=models.CharField(default=0, max_length=500, verbose_name='Tahmini Süre'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='joblist',
            name='Tarih',
            field=models.CharField(default=0, max_length=500, verbose_name='Tarih'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='joblist',
            name='TeknikUzman',
            field=models.CharField(default=0, max_length=500, verbose_name='Teknik Uzman'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todos',
            name='todoAciklama',
            field=models.CharField(default=0, max_length=500, verbose_name='Açıklama'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todos',
            name='todoDurum',
            field=models.CharField(default=0, max_length=500, verbose_name='Durum'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todos',
            name='todoTarih',
            field=models.CharField(default=0, max_length=500, verbose_name='Tarih'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todos',
            name='todoYapilacakIs',
            field=models.CharField(default=0, max_length=500, verbose_name='Yapılacak İş'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todos',
            name='TodosJob',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Uygulama.joblist', verbose_name='Hangi iş?'),
        ),
    ]