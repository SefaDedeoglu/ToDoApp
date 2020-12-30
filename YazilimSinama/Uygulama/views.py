from django.shortcuts import render,redirect,HttpResponse
from .models import JobList
# Create your views here.
def main(request):
    
    return render(request,"MainMenu.html")

def uygulama(request):
    Joblist1 = JobList.objects.all()
    return render(request,"index.html",{"JobList":Joblist1})