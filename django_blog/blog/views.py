from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, UserProfileForm
from django.contrib.auth.decorators import login_required


# Create your views here.

'''This function creates the registration view 
using the custom UserCreationForm'''

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully')
            return redirect('home')

    else:
            form = CustomUserCreationForm()

    return render(request, 'blog/register.html', {'form': form})


'''This function creates the view 
for the Django ModelForm, UserProfileForm 
The decorator @login_required ensures only logged in users can access and edit profile
''' 

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileModelForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
            return redirect("profile")
        else:
            form = ProfileModelForm(instance=request.user.userprofile)

    return render(request, 'blog/profile.html', {'form': form})


'''defining a home view '''
def home(request):
    return render(request, 'blog/home.html')


'''defining a view to list post instances'''
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

