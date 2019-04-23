from django.views.generic import DetailView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

from django.shortcuts import render


def redirect_to_user_profile(request):
    if request.user.is_authenticated:
        print(request.user.pk)
        redirect_url = f"{request.user.pk}/"
        return HttpResponseRedirect(redirect_to=redirect_url)


class UserProfile(DetailView):
    model = User
    template_name = 'user_profile.html'
    context_object_name = 'user'


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = '/accounts/login/'
    template_name = 'signup.html'


