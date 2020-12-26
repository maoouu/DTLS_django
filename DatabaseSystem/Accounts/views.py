from django.shortcuts import redirect, render
from .forms import RegisterForm


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/home/dashboard")
    else:
        form = RegisterForm()

    return render(response, "Accounts/register.html", {"form": form})
