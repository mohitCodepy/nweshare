from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
import pyautogui as sm
from .models import RUserdata, Notes
from django.contrib.auth.decorators import login_required
from datetime import date

# Create your views here.


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def register(request):
    if request.method == "POST":
        Name = request.POST["Name"]
        Username = request.POST["userName"]
        Email = request.POST["Email"]
        Phone_no = request.POST["Phone_no"]
        Password = request.POST["Password"]
        CmfPassword = request.POST["CmfPassword"]
        Role = request.POST["role"]
        Branch = request.POST["branch"]
        Clg_Year = request.POST["year"]
        if Password == CmfPassword:
            if User.objects.filter(username=Username).exists():
                sm.alert("User already exists")
                return redirect("registration.html")
            elif User.objects.filter(email=Email).exists():
                sm.alert("Email already exists")
                return redirect("registration.html")
            else:
                try:
                    x = User.objects.create_user(
                        username=Username, email=Email, password=Password
                    )
                    RUserdata.objects.create(
                        user=x,
                        Name=Name,
                        Phone_no=Phone_no,
                        Role=Role,
                        Branch=Branch,
                        Clg_Year=Clg_Year,
                    )
                    x.save()
                    sm.confirm("user created")
                    return render(request, "login.html")
                except:
                    return render(request, "registration.html")
        else:
            sm.alert("password not matching")
            return redirect("registration.html")
    else:
        return render(request, "registration.html")


def login(request):
    if request.method == "POST":
        username1 = request.POST["user"]
        password1 = request.POST["p"]
        users = auth.authenticate(username=username1, password=password1)
        try:
            if users is not None:
                auth.login(request, users)
                param = {"name": username1}
                return render(request, "registration.html", param[1])
            else:
                return render(request, "registration.html")
        except:
            return redirect("/")
    else:
        return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect("/")


@login_required(login_url="login")
def share(request):
    return render(request, "sharepage.html")


def upload(request):
    if not request.user.is_authenticated:
        return redirect("login")
    error = ""
    if request.method == "POST":
        b = request.POST["branch"]
        s = request.POST["subject"]
        t = request.POST["type"]
        u = request.FILES["upload"]
        d = request.POST["desc"]
        ct = User.objects.filter(username=request.user.username).first()
        try:
            Notes.objects.create(
                user=ct,
                Date=date.today(),
                Branch=b,
                Subject=s,
                Type=t,
                Uploadfile=u,
                Desc=d,
            )
            ct.save()

            return redirect("viewmydata")
        except:
            return render(request, "upload.html")
    else:
        return render(request, "upload.html")


def viewmydata(request):
    user = User.objects.get(id=request.user.id)
    notes = Notes.objects.filter(user=user)
    nt = {"notes": notes}
    return render(request, "viewmydata.html", nt)


def viewallnotes(request):
    v = Notes.objects.all()
    vv = {"data": v}
    return render(request, "viewallnotes.html", vv)


def search(request):
    if request.method == "GET":
        s = request.GET.get("search")
        v = Notes.objects.all().filter(Desc__icontains=s)
        vv = {"data": v}
        return render(request, "search.html", vv)
