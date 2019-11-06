from django.shortcuts import render,redirect
from . forms import *
from . models import *


# Create your views here.
def index(request):
    form=StudentForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(view)
    else:
        return render(request,'index.html',{'form':form})


def view(request):
    data=Student.objects.filter()
    return render(request,'view.html',{'data':data})

def update(request,pk):
    if request.method=='POST':
        data=Student.objects.get(pk=pk)
        form=StudentForm(request.POST or None ,instance=data)
        if form.is_valid():
            form.save()
            return redirect(view)
    
    data=Student.objects.get(pk=pk)
    form=StudentForm(instance=data)
    return render(request,'update.html',{'form': form , 'data': data})

    

def delete(request,pk):
    data=Student.objects.get(pk=pk)
    data.delete()
    data=Student.objects.all()
    return render(request,"view.html",{'data':data})