from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from users.forms import SignUpForm
from users.models import DeliveryAddress


class PersonalArea(DetailView):
    model = DeliveryAddress
    template_name = 'users/personal_area.html'


class SignUpView(View):
    template_name = 'users/sign_up.html'

    def get(self, request):
        context = {
            'form': SignUpForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main')
        context = {
            'form': form
            }
        return render(request, self.template_name, context)


class SignInView(LoginView):
    template_name = 'users/sign_in.html'


def logout_user(request):
    logout(request)
    return redirect('main')
