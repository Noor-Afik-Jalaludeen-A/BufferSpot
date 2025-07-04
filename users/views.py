from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import userRegistrationForm, userUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = userRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(username)
            messages.success(request, f'Your account has been created! You can now log in {username}.')
            return redirect('login')  # Redirect to the login page after successful registration
        else:
            print("Form is not valid")
            print(form.errors)
            return render(request, 'users/register.html', {'form': form})
    else:
        form = userRegistrationForm()
    return render(request, 'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method=='POST':
        u_form = userUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    u_form = userUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,   
        'p_form': p_form
    }
    return render(request, 'users/profile.html',{'context': context})