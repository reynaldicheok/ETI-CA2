"""ToDoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include #new
from todo.views import todo_view, add_todo, delete_todo, check_login, todo_viewhistory
from django.views.generic.base import TemplateView # new
from django.conf.urls import url
from Login.views import signup
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('todo/',todoView),
    
    #path('todo/', TemplateView.as_view(template_name='todo.html')),
    path('todo/', todo_view),
    path('addTodo/', add_todo),
    path('deleteTodo/<int:todo_id>/', delete_todo),
    path('accounts/', include('django.contrib.auth.urls')),
    path('history/',todo_viewhistory),
    path('signup/', signup),
    
    # new
]
