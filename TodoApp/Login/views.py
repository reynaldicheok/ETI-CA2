from django.shortcuts import render
from django.http import HttpResponse
#from django.contrib.auth import login,logout,authenticate

# Create your views here.
def todoView(request):
    return render(request,'todo.html')

