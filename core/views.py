from django.shortcuts import render, redirect
from django.contrib.auth import login
from . import forms
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Django Deployed</h1>")
    return render(request,'home.html')

def sign_up(request):
    form  = forms.SignUpForm()
    if request.method=='POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email').lower()

            user  = form.save(commit=False)
            user.username=email
            user.save()

            login(request,user)
            return redirect('/') 
    return render(request,'sign_up.html',{
        'form':form
    })