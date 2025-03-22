from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, UserProfileForm, CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404, redirect


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
    form = None
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
            return redirect("profile")
        else:
            form = UserProfileForm(instance=request.user.userprofile)

    return render(request, 'blog/profile.html', {'form': form})


'''defining a view to list Post instances'''
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


''' creating Use Django’s class-based views to handle CRUD operations 
    with Post model by extending ListView, DetailView, CreateView, 
    UpdateView, DeleteView '''

# Custom Based View to list all Post instances/objects
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

# Custom Based View to fetch detail of a Post instance
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'posts'

#import mixin to ensure only logged-in users can create Post instances
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'author']
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#import mixins to ensure only logged in authors can update Post instance
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user  # Ensure author remains the same
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()  # Get the current post instance
        #only allow author to update
        return self.request.user == post.author

#import mixins to ensure only logged in author can delete Post instance
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')  # Redirect after deletion

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author



''' creating Use Django’s class-based views to handle CRUD operations           with Comment model by extending ListView, DetailView, CreateView,              UpdateView, DeleteView '''


class CommentListView(ListView):
    model = Comment
    template_name = "blog/comment_list.html"
    context_object_name = "comments"

    def get_queryset(self):
        """Get comments for a specific blog post."""
        post = get_object_or_404(Post, id=self.kwargs["post_id"])
        return post.comments.all()

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def form_valid(self, form):
        """Assign the comment to the logged-in user and post."""
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, id=self.kwargs["post_id"])
        return super().form_valid(form)

    def get_success_url(self):
        """Redirect back to the post detail page after comment creation."""
        return reverse("post_detail", kwargs={"pk": self.kwargs["post_id"]})

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def test_func(self):
        """Ensure only the comment author can edit."""
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        """Redirect back to the post detail page after editing."""
        return reverse("post_detail", kwargs={"pk": self.object.post.id})

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "blog/comment_confirm_delete.html"

    def test_func(self):
        """Ensure only the comment author can delete."""
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        """Redirect back to the post detail page after deletion."""
        return reverse("post_detail", kwargs={"pk": self.object.post.id})
