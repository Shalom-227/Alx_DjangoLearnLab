from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy


# Create your views here.


'''defining a home view '''
def home(request):
    return render(request, 'blog/home.html')


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


'''defining a view to list post instances'''
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


'''creating Use Django’s class-based views to handle CRUD operations
   by extending ListView, DetailView, CreateView, UpdateView, DeleteView '''
# Custom Based View to list all objects
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'posts'

#import decorators to ensure only logged in users can create Post instance
@method_decorator(login_required, name='dispatch')
class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'published_date', 'author']
    success_url = reverse_lazy('post_list')


#import decorators to ensure only logged in users can edit Post instance
@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'author']
    success_url = reverse_lazy('post_list')

    def get_object(self, queryset=None):
        return super().get_object(queryset)

#import decorators to ensure only logged in users can delete Post instance
@method_decorator(login_required, name='dispatch')
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def get_object(self, queryset=None):
        return super().get_object(queryset)

