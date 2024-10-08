from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print('Signup successfully, redirecting to Login Page.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html',{'form': form})

def landing_page(request):
    if request.user.is_authenticated:
        return redirect('login')
    return redirect('signup')
