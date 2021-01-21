from django.db import models

# Create your models here.
class JobList(models.Model):
    ProjeNo=models.CharField(max_length = 500,verbose_name ="Proje No",null=False, blank=True, default=00000)
    TeknikUzman = models.CharField(max_length = 500, verbose_name="Teknik Uzman",null=False, blank=True, default=00000)
    TahminiSure = models.CharField(max_length=500,verbose_name="Tahmini Süre",null=False, blank=True, default=00000)
    GerceklesenSure=models.CharField(max_length=500,verbose_name="Gerçekleşen Süre",null=False, blank=True, default=00000)
    Tarih = models.CharField(max_length=500,verbose_name="Tarih",null=False, blank=True, default=00000)
    KartNo = models.CharField(max_length=500,verbose_name="Kart No",null=False, blank=True, default=00000)
    IsAciklamasi = models.CharField(max_length=500,verbose_name="İş Açıklaması",null=False, blank=True, default=00000)
    Notlar = models.CharField(max_length=500,verbose_name="Notlar",null=False, blank=True, default=00000)
    def __str__(self):
         return "id: {} || Proje Adı/No {}".format(self.id,self.ProjeNo)

class Todos(models.Model):
    TodosJob = models.ForeignKey(JobList,on_delete=models.CASCADE,verbose_name="Hangi iş?")
    todoTarih = models.CharField(max_length=500,verbose_name="Tarih",null=False, blank=True, default=00000)
    todoDurum = models.CharField(max_length=500,verbose_name="Durum",null=False, blank=True, default=00000)
    todoYapilacakIs= models.CharField(max_length=500,verbose_name="Yapılacak İş",null=False, blank=True, default=00000)
    todoAciklama = models.CharField(max_length=500,verbose_name="Açıklama",null=False, blank=True, default=00000)


    def __str__(self):
        
        return "id: {} || bağlı olunan iş : // {} // ".format(self.id,self.TodosJob)

        

