from django.shortcuts import render,redirect
from .models import Value
from django.http import HttpResponse
# Create your views here.
def home(request):
    myData=Value.objects.all()
    if(myData!=''):
        return render(request,'home.html',{'datas':myData})
    else:
        return render(request,'home.html')


def addData(request):
    if request.method=='POST':
        vname=request.POST['vname']
        vClass=request.POST['vClass']
        vsection=request.POST['vsection']
        vrollno=request.POST['vrollno']

        obj=Value()
        obj.Name=vname
        obj.Class=vClass
        obj.Section=vsection
        obj.Rollno=vrollno
        obj.save()

        myData=Value.objects.all()
        return redirect('home')


    return render(request,'home.html')

def updateData(request,id):
    myData=Value.objects.get(id=id)
    if request.method=='POST':
        vname=request.POST['vname']
        vClass=request.POST['vClass']
        vsection=request.POST['vsection']
        vrollno=request.POST['vrollno']

        myData.Name=vname
        myData.Class=vClass
        myData.Section=vsection
        myData.Rollno=vrollno
        myData.save()

        
        return redirect('home')
    return render(request,'update.html',{'datas':myData})

def deleteData(request,id):
     myData=Value.objects.get(id=id)
     myData.delete()
     return redirect('home')
