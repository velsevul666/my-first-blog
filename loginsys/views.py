# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, render,  redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect
# from .forms import LoginForm, UserRegistrationForm


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Пользователь не найден"
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)

    # if request.method == 'POST':
    #     form = LoginForm(request.POST)
    #     if form.is_valid():
    #         cd = form.cleaned_data
    #         user = authenticate(username=cd['username'], password=cd['password'])
    #         if user is not None:
    #             if user.is_active:
    #                 auth.login(request, user)
    #                 return redirect('post_list')
    #             else:
    #                 print('disabled account')
    #                 return render(request,
    #                               'loginsys/error.html')
    #         else:
    #             print('incorrect password')
    #             return render(request,
    #                           'loginsys/error.html')
    # else:
    #     form = LoginForm()
    #     print('1')
    # return render(request, 'login.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password = newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render_to_response('register.html', args)
    # if request.method == 'POST':
    #     user_form = UserRegistrationForm(request.POST)
    #
    #     if user_form.is_valid():
    #         # Create a new user object but avoid saving it yet
    #         new_user = user_form.save(commit=False)
    #         # Set the chosen password
    #         new_user.set_password(user_form.cleaned_data['password'])
    #         # Save the User object
    #         new_user.save()
    #
    #         return redirect('/loginsys/login/')
    # else:
    #     user_form = UserRegistrationForm()
    # return render(request, 'loginsys/register.html', {'user_form': user_form})