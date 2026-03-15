from django.shortcuts import render
#it renders the view (render means run)

def home(request):
    return render(request,'home.html')
