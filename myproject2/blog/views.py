from django.http import HttpResponse

def post_details(response,post_id):
    return HttpResponse(f"<h1>show blog post{post_id}</>")

def user_profile(response,username):
    return HttpResponse(f"<h1> profile of the user {username}")

def dates(response,**kwargs):
    return HttpResponse(f"<h1> Date is {kwargs}</h1>")
