from django.db import models

# Create your models here.
class JobList(models.Model):
    title=models.CharField(max_length = 50,verbose_name ="Başlık")
    ToDoCount = models.IntegerField(verbose_name="Durum")
    text = models.CharField(max_length = 150, verbose_name="Yazı")
    photo = models.CharField(max_length=200,verbose_name="Fotoğraf")
    def __str__(self):
        return self.title