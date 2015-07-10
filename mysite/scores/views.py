from django.shortcuts import render
from django.http import HttpResponseRedirect

def index(request):
    return HttpResponseRedirect('login')

def login(request):
    #tempalte = loader.get_template('scores/login.html')
    return render(request, 'scores/login.html', {})

#def user(request, user_name, user_pwd):
def user(request):
    return render(request, 'scores/user.html', {})
