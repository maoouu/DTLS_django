from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(response):
    return redirect("/dashboard")


@login_required(login_url="../login")
def dash(response):
    return render(response, "EnvergaDB/dashboard.html", {})
