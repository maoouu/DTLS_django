from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Records  # models.py
from .forms import RecordForm  # forms.py


# Create your views here.
def index(response):
    return redirect("/dashboard")


@login_required(login_url="../login")
def dash(response):
    records = Records.objects.all()
    return render(response, "EnvergaDB/dashboard.html", {'records': records})


@login_required(login_url="../login")
def add(response):
    if response.method == "POST":
        form = RecordForm(response.POST)
        if form.is_valid:
            try:
                form.save()
                messages.success(
                    response, 'Item has been successfully added to the database.')
                return redirect("/dashboard")
            except:
                pass
    else:
        form = RecordForm()
    return render(response, "EnvergaDB/add.html", {'form': form})


@login_required(login_url="../login")
def update(response, id):
    record = Records.objects.get(id=id)
    update_form = RecordForm(instance=record)
    if response.method == "POST":
        form = RecordForm(response.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(
                response, 'Item has been updated.')
            return redirect("/dashboard")
    return render(response, "EnvergaDB/edit.html", {'form': update_form, 'record': record})


@login_required(login_url="../login")
def delete(response, id):
    Records.objects.filter(id=id).delete()
    messages.info(response, 'Item has been deleted.')
    return redirect("/dashboard")
