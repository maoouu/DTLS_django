from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
            messages.success(response, 'Account created successfully')
            return redirect("../login")
    else:
        form = UserCreationForm()

    return render(response, "Accounts/register.html", {"form": form})
