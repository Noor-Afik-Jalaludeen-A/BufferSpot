from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Count
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q



# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Afik',
    }
    return render(request, 'Blog/Home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'Blog/Home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4 # Number of posts per page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        top_authors = User.objects.annotate(post_count=Count('post')).order_by('-post_count')[:5]
        trending_posts = Post.objects.order_by('-views')[:5]  # 👈 Add this
        context['top_authors'] = top_authors
        context['trending_posts'] = trending_posts  # 👈 Include in context
        return context

    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query) | Q(author__username__icontains=query)
            ).order_by('-date_posted')
        return Post.objects.all().order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
    template_name = 'Blog/Post_detail.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if self.request.user != obj.author:
            obj.views = obj.views + 1
            obj.save(update_fields=['views'])  # ensures only the views field is updated
        return obj
    
    

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'Blog/Post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'Blog/Post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'Blog/Post_confirm_delete.html'
    success_url = reverse_lazy('blog-home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class UserPostListView(ListView):
    model = Post
    template_name = 'Blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 2 # Number of posts per page

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

def about(request):
    return render(request, 'Blog/About.html')

def announcements(request):
    context = {
        'title': 'Announcements',
    }
    return render(request, 'Blog/announcement.html', context)

def event(request):
    return render(request, 'Blog/event.html', {'title': 'Events'})

def resources(request):
    return render(request, 'Blog/resources.html', {'title': 'Resources'})

def contact(request):
    return render(request, 'Blog/contact.html', {'title': 'Contact Us'})