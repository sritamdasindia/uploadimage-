from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.core.files.storage import FileSystemStorage
# Create your views here.
def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        if email == "admin" and password == "admin":
            request.session['username'] = email
            return JsonResponse({"status":"success","message":"Login successful"})
        else :
            return JsonResponse({"status":"failed","message":"Login Failed"})
    elif request.method == "GET":
        return render(request,"interact/login.html")

def signup(request):
    if request.method=="POST":
        image = request.FILES["image"]
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)
        p = Profile(profilepic=uploaded_file_url,name=name, password=password,email=email)
        p.save(force_insert=True)
        print(image)
        return JsonResponse({"status":"success"})
    return render(request,"interact/signup.html")

def error(request):
    return

def dashboard(request):
    if request.session.has_key("username"):
        return JsonResponse({"message":"Welcome to dashboard"})
    return
