from django.shortcuts import render
from django.http import HttpResponse
from .models import*


# Create your views here.
def home(request):
    
    if request.method == "POST":
        data = request.POST
        
        image=request.FILES.get("image")
        name=data.get('name')
        age=data.get('age')
        address=data.get('address')
        email=data.get('email')
        
        student.objects.create(
            name=name,
            age=age,
            email=email,
            address=address,
            image=image,
        )
        
    return render(request , "home/index.html")

