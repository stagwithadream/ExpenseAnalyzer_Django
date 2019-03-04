from django.shortcuts import render
from django.http import HttpResponse
from . import models
from . import forms
# Create your views here.

def dashboard(request):
    return render(request,'examples/dashboard.html')

def user(request):
    user
    return render(request,'examples/user.html')

def summary(request):
    return render(request,'examples/summary.html')

def debts(request):
    return render(request,'examples/debts.html')

def mandatory(request):
    return render(request,'examples/mandatory.html')

def analyze(request):
    return render(request,'examples/analyze.html')

def notification(request):
    return render(request,'examples/notification.html')

def addExpense(request):
    form=forms.addExpense_form()
    my_form={'form':form}

    if request.method=="POST":
            form=forms.addExpense_form(request.POST)

            if form.is_valid():
                form.save()
                return dashboard(request)

    return render(request,'examples/AddExpense.html',my_form)

def addMoney(request):
    return render(request,'examples/AddMoney.html')
