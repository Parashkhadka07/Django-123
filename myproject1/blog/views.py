from django.http import HttpResponse

def home(request):
    return HttpResponse("blog home page")

def about(request):
    return HttpResponse("<h1>vlog about page</h1>")