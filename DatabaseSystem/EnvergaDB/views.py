from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Records  # models.py
# Create your views here.


def index(response):
    return redirect("/dashboard")


@login_required(login_url="../login")
def dash(response):
    records = Records.objects.all()
    return render(response, "EnvergaDB/dashboard.html", {'records': records})
