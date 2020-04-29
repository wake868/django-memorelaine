from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import UserProfileForm, UserForm
from .models import UserProfile


@login_required
def home(request):
    user = get_object_or_404(User, pk=request.user.id)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect('userprofiles:home')
    else:
        form = UserForm(instance=user)
    
    context = {'user': user, 'form': form}
    return render(request, 'userprofiles/home.html', context)


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # profile_form = UserProfileForm(request.POST)

        # if form.is_valid() and profile_form.is_valid():
        if form.is_valid():
            user = form.save()

            profile = UserProfile()
            profile.user = user
            profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('userprofiles:home')

    else:
        form = UserCreationForm()
        # profile_form = UserProfileForm()

    # context = {'form': form, 'profile_form': profile_form}
    context = {'form': form}
    return render(request, 'userprofiles/register.html', context)


def login_user(request):
    if request.method == 'GET':
        return render(request, 'userprofiles/login.html', {'form': AuthenticationForm()})
    else:
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
            if user is None:
                return render(request, 'userprofiles/login.html', {'form': AuthenticationForm(), 'error': 'Username or password is invalid.'})
            else:
                login(request, user)
                return redirect('userprofiles:home')


@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('userprofiles:home')
