from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
def main(request):
    return render(request,"MainMenu.html")