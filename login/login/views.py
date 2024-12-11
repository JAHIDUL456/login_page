from django.shortcuts import render


#lets controlt the views of each apages

def homepage(request):
    return render(request,'home.html')

def signup(request):
    return render(request,'signup.html')

def login(request):
    return render(request,'login.html')