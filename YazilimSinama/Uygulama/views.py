from django.shortcuts import HttpResponse, render,redirect,get_object_or_404,HttpResponseRedirect
from .models import JobList
from .models import Todos
from django.urls import reverse


# Create your views here.
def main(request):
    JobList1 = JobList.objects.all()
    return render(request,"MainMenu.html",{"JobList1":JobList1})

def uygulama(request,id):
    Joblist1 = get_object_or_404(JobList,id=id)
    todos1 = Todos.objects.all()
    if request.method == "POST":
        pass
    else:
        return render(request,"index.html",{"Joblist1":Joblist1,"todos1":todos1})

    

def isEkle(request):
    if(request.method=="GET"):
        return render(request,"isEkle.html")
    else:
        return render(request,"isEkle.html")
       
    
def isEkleAction(request):
    if request.method=="POST":
        projeno=request.POST.get("projeNo")
        kartno = request.POST.get("kartNo")
        tarih = request.POST.get("tarih")
        teknikUzman = request.POST.get("teknikUzman")
        tahminiSure = request.POST.get("tahminiSure")
        gerceklesenSure = request.POST.get("gerceklesenSure")
        isAciklamasi = request.POST.get("isAciklamasi")
        notlar = request.POST.get("notlar")
        newjob = JobList(ProjeNo=projeno,TeknikUzman=teknikUzman,TahminiSure=tahminiSure,GerceklesenSure=gerceklesenSure,Tarih=tarih,KartNo=kartno,IsAciklamasi=isAciklamasi,Notlar=notlar)
        newjob.save()
        int1 = request.POST.get("sayac")
        todoCount = int(int1)
        for i in range(0,todoCount):
            ta= "t"+str(i+1)
            da= "d"+str(i+1)
            ya = "y"+str(i+1)
            aa = "a"+str(i+1)
            TodoTarih =request.POST.get(""+ta+"")
            TodoDurum =request.POST.get(""+da+"")
            TodoYapilacakis =request.POST.get(""+ya+"")
            TodoAciklama = request.POST.get(""+aa+"")
            TodoJob = newjob
            
            Todo = Todos(TodosJob=TodoJob,todoTarih=TodoTarih,todoDurum=TodoDurum,todoYapilacakIs=TodoYapilacakis,todoAciklama=TodoAciklama)
            Todo.save()

        return redirect("/")
    else:
        return render(request,"index.html")

def isDuzenle(request,id):
    nesne = get_object_or_404(JobList,id=id)
    Todos1 = Todos.objects.all()
    i=0
    if(nesne):
        if(Todos1):
            for item in Todos1:
                if(item.TodosJob==nesne):
                    i+=1


            
    return render(request,"isGuncelle.html",{"nesne":nesne,"Todos1":Todos1,"i":i})
    

def isGuncelleAction(request,id):
    nesne = get_object_or_404(JobList,id=id)
    nesne.ProjeNo = request.POST.get("projeNo")
    nesne.KartNo = request.POST.get("kartNo")
    nesne.Tarih = request.POST.get("tarih")
    nesne.TeknikUzman = request.POST.get("teknikUzman")
    nesne.TahminiSure = request.POST.get("tahminiSure")
    nesne.GerceklesenSure = request.POST.get("gerceklesenSure")
    nesne.IsAciklamasi = request.POST.get("isAciklamasi")
    nesne.Notlar = request.POST.get("notlar")
    nesne.save()
    sayac=0
    items = Todos.objects.all()
    for item in items:
        if item.TodosJob == nesne:
            sayac+=1

    int1 = request.POST.get("sayac")
    todoCount = int(int1)
    
    for i in range(0,sayac):
        ta= "t"+str(i+1)
        da= "d"+str(i+1)
        ya = "y"+str(i+1)
        aa = "a"+str(i+1)
        id1 = "id"+str(i+1)
        getid = request.POST.get(""+id1+"")
        Todo = get_object_or_404(Todos,id=getid)
        Todo.TodosJob=nesne
        Todo.todoTarih=request.POST.get(""+ta+"")
        Todo.todoDurum =request.POST.get(""+da+"")
        Todo.todoYapilacakIs = request.POST.get(""+ya+"")
        Todo.todoAciklama = request.POST.get(""+aa+"")
        Todo.save()


    for i in range(sayac,todoCount):
        ta= "t"+str(i+1)
        da= "d"+str(i+1)
        ya = "y"+str(i+1)
        aa = "a"+str(i+1)
        TodoTarih =request.POST.get(""+ta+"")
        TodoDurum =request.POST.get(""+da+"")
        TodoYapilacakis =request.POST.get(""+ya+"")
        TodoAciklama = request.POST.get(""+aa+"")
        TodoJob = nesne
        Todo = Todos(TodosJob=TodoJob,todoTarih=TodoTarih,todoDurum=TodoDurum,todoYapilacakIs=TodoYapilacakis,todoAciklama=TodoAciklama)
        Todo.save()
    return redirect("/")
    
def todos(request,id):
    todo = get_object_or_404(Todos,id=id)
    a = JobList.objects.all()
    id = 1
    for item in a :
        if item == todo.TodosJob:
            id=item.id
            break
    return render(request,"todos.html",{"todo":todo,"id":id})
def todoEkle(request,durum,id):
    return render(request,"todoEkle.html",{"durum":durum,"id":id})
    
def eklendi(request,id):
    tarih = request.POST.get("t")
    durum = request.POST.get("d")
    yapilacak = request.POST.get("y")
    aciklama = request.POST.get("a")
    job = get_object_or_404(JobList,id=id)
    todo = Todos(TodosJob=job,todoTarih=tarih,todoDurum=durum,todoYapilacakIs=yapilacak,todoAciklama=aciklama)
    todo.save()
    
    return HttpResponseRedirect(reverse(uygulama, args=(id,)))
def updatetodo(request,id):
    todo = get_object_or_404(Todos,id=id)
    tarih = request.POST.get("t")
    durum = request.POST.get("d")
    yapilacak = request.POST.get("y")
    aciklama = request.POST.get("a")
    todo.todoTarih=tarih
    todo.todoDurum=durum
    todo.todoYapilacakIs=yapilacak
    todo.todoAciklama=aciklama
    todo.save()
    a = JobList.objects.all()
    id = 1
    for item in a :
        if item == todo.TodosJob:
            id=item.id
            break
    return HttpResponseRedirect(reverse(uygulama, args=(id,)))

def deletetodo(request,id):
    todo = get_object_or_404(Todos,id=id)
    a = JobList.objects.all()
    id = 1
    for item in a :
        if item == todo.TodosJob:
            id=item.id
            break
    todo.delete()
    return HttpResponseRedirect(reverse(uygulama, args=(id,)))

def todoGoruntule(request,id):
    todo = get_object_or_404(Todos,id=id)
    a = JobList.objects.all()
    id = 1
    for item in a :
        if item == todo.TodosJob:
            id=item.id
            break
    return render(request,"todoGoruntule.html",{"todo":todo,"id":id})

def dragdrop(request,durum,id):
    todo = get_object_or_404(Todos,id=id)
    a = JobList.objects.all()
    id = 1
    for item in a :
        if item == todo.TodosJob:
            id=item.id
            break
    if durum ==1:
        todo.todoDurum="Eklendi"
        todo.save()
    elif durum==2:
        todo.todoDurum="Yapım Aşamasında"
        todo.save()
    elif durum==3:
        todo.todoDurum = "Bitti"
        todo.save()
    elif durum==4:
        todo.delete()
    else :
        pass
    return HttpResponseRedirect(reverse(uygulama, args=(id,)))

