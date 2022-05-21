from django.http import HttpResponseRedirect
from django.contrib.auth import logout
# Create your views here.
from django.shortcuts import render, redirect
from .models import Studentmodel
from .forms import StudentForm, AddCourseForm,FeeForm


def indexView(request):
    data=Studentmodel.objects.all()
    print("data")
    return render(request,'index.html',{'data2':data})

def studentView(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentForm()
    return render(request,'studentcreate.html',{'form':form})


def courseView(request):
    if request.method == "POST":
        form= AddCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AddCourseForm()
    return render(request,'courseadd.html',{'form':form})

def feeView(request):
    inputO = request.POST.get('inputO')
    if request.method =="POST":
        form = FeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = FeeForm()
    return render(request,'fee.html',{'form':form})

def Home(request):

    return render(request,'home.html')

def logout(request):
    """Logs out user"""
    logout(request)
    return HttpResponseRedirect('/')