from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"main/index.html")
context={
    "0":{},
    "1":{
        "project":"ironman",
        "role":"lead engineear"
    },
    "2":{
        "project":"hulk",
        "role":"physichist"
    }
}
def projects(request,id=None):
    print("the id of the sanskari project is ",id)
    if id is None:
        return render(request,"main/projects.html")
    
    project=context[id]
   
    contextt={
        "details":project
    }
    print()
    return render(request,"main/projects.html",contextt)

       
    
def contact(request):
    return render(request,"main/contact.html")
