from django.shortcuts import redirect, render
from .models import *
from django.http import HttpResponse

# Create your views here.
def rescipe(request):
    if request.method == "POST":
        data = request.POST
        
        rescipe_image=request.FILES.get("rescipe_image")
        rescipe_name = data.get('rescipe_name')
        rescipe_description = data.get('rescipe_description')
        
        Rescipe.objects.create(
            rescipe_name = rescipe_name,
            rescipe_image = rescipe_image,
            rescipe_description = rescipe_description,
            )
       
        return redirect("/rescipe/")
    
    queryset = Rescipe.objects.all()  
    context = {'rescipe': queryset}
    
    
    return render(request , "rescipe.html", context)

def update_rescipe(request, id):
    queryset= Rescipe.objects.get(id = id)
    
    if request.method == "POST":
        data=request.POST
        
        rescipe_image = request.FILES.get("rescipe_image")
        rescipe_name = data.get('rescipe_name')
        rescipe_description = data.get('rescipe_description')
        
        queryset.rescipe_name = rescipe_name
        queryset.rescipe_description=rescipe_description
        
        if rescipe_image:
            queryset.rescipe_image = rescipe_image
            
        queryset.save()
        return redirect("/rescipe/")
        
        
        
    context = {'rescipe': queryset}
    return render(request , "update_rescipe.html", context) 

def delete_rescipe(request, id):
    queryset= Rescipe.objects.get(id = id)
    queryset.delete()
    return redirect("/rescipe/")


    
    
    