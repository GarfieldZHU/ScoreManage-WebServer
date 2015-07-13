#coding=utf-8

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import *


def index(request):
    return render_to_response('scores/login.html', {})

@csrf_exempt
def login(request):
    #tempalte = loader.get_template('scores/login.html')
    #return render(request, 'scores/login.html', {})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #print username, password
        if username == 'admin' and password == 'admin':
            return render_to_response('scores/manage.html', {'person_name': '管理员'})
        elif Student.objects.filter(sid=username, spwd=password):
            name = Student.objects.get(sid=username).sname
            return render_to_response('scores/student.html', {'person_name': name})
        elif Teacher.objects.filter(tid=username, tpwd=password):
            name = Teacher.objects.get(tid=username).tname
            return render_to_response('scores/teacher.html', {'person_name': name})

    return render_to_response('scores/login.html', {})

#def user(request, user_name, user_pwd):
def user(request):
    #return render(request, 'scores/user.html', {})
    return render_to_response('scores/user.html', {})

def logout(request):
    return render_to_response('scores/logout.html',{})
