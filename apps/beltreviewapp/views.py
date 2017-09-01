# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

def index(request):
    return render(request , 'beltreviewapp/index.html')

def register(request):
    #gets info from UserManger
    errs = User.objects.validate_reg(request.POST)
    #if there are any errors from the errors[] list. it will not go through
    if errs:
        for e in errs:
            messages.error(request, e)
    else:
        #make user if no errors
        new_user = User.objects.create_user(request.POST)
        request.session['id'] = new_user.id
        messages.success(request, 'thank you {} for registering'.format(new_user.full_name))
    return redirect('/')
