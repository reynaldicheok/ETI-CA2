from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem , TodoItemHistory
from datetime import date


def todo_viewhistory(request):
    if request.user.is_authenticated:      
        print("Success")
    else:
        return HttpResponseRedirect('/accounts/login')
        print("Fail")

    all_todo_items = TodoItemHistory.objects.all()
    return render(request, 'todohistory.html',
        {'all_items': all_todo_items})

def todo_view(request):
    if request.user.is_authenticated:      
        print("Success")
    else:
        return HttpResponseRedirect('/accounts/login')
        print("Fail")
    all_todo_items = TodoItem.objects.filter(user=request.user)
    return render(request, 'todo.html',
        {'all_items': all_todo_items})

def add_todo(request):
    
    new_item = TodoItem(content = request.POST['content'],timestamp = date.today(),user=request.user)
    new_item.save()
    history_item = TodoItemHistory(content = request.POST['content'],timestamp = date.today())
    history_item.save()
    return HttpResponseRedirect('/todo/')

def delete_todo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')

def check_login(request):
    
    if request.user.is_authenticated:
        
        return HttpResponseRedirect('/todo/')
        print("Success")
    else:
        return HttpResponseRedirect('/accounts/login')
        print("Fail")
