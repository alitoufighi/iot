# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Message
from django.core import serializers
# Create your views here.
def home(request):
    if request.method == 'POST':
        if 'logout' in request.POST:
            request.session['username'] = None
            return render(request, 'testapp/login.html')
        elif 'explanation' in request.POST and 'title' in request.POST:
            print(request.POST)
            explanation=request.POST['explanation']
            title=request.POST['title']
            msg = Message.objects.create(title=title, explanation=explanation)
            msg.save()
            Message.objects.all()
            return render(request, 'testapp/home.html', {'msg': 'Your Message Has Been Saved.'})
        else:
            username = request.POST['username']
            password = request.POST['password']
            request.session['username']=username
            if username == 'admin' and password == '1234':
                return render(request, 'testapp/home.html', {'msg': None})
            else:
                return render(request, 'testapp/login.html', {'err':'User info is not valid.'})
    else:
        username=request.session.get('username', None)
        if username != None:
            return render(request, 'testapp/home.html', {'msg': None})
        else:
            return render(request, 'testapp/login.html', {'err':None})
def log(request):
    if request.method == 'GET':
        if 'username' in request.session:
            # messages = Message.objects.all()
            # messages_str = messages.__str__()
            data = serializers.serialize("json", Message.objects.all())
            return render(request, 'testapp/log.html', {'data': data})

# def logout(request):
#     request.session['username'] = None
#     return render(request, 'testapp/login.html')