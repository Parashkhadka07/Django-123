from django.http import HttpResponse

def home(request):
    return HttpResponse("shop home page")

def about(request):
    return HttpResponse("<h1>shop about page</h1>")

def products(request):
    return HttpResponse("ahop product page")