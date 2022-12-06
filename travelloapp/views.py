from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Place
from .models import Testimonia
def fun(request):
    obj=Place.objects.all()
    obj1=Testimonia.objects.all()

    return render(request,'index.html',{'results':obj,'obj1':obj1})
def fun1(request):
    obj1=Testimonia.objects.all()
    return render(request,'index.html',{'obj1':obj1})
