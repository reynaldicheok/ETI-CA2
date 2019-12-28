from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
#from django.contrib.auth import login,logout,authenticate

# Create your views here.
def todoView(request):
    return render(request,'todo.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('username')
            email = email + '123@gmail.com'
            #form = FormName(commit=False)
            new_password=make_password(raw_password)
            #form.save()
            #user = authenticate(username=username, password=raw_password)
            new_user = User.objects.create(username=username, email=email, password=new_password)
            #new_user = form.save(commit=False)
            new_user.save()

            return redirect('../accounts/login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

