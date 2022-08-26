from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Announcement


# a list view for the blog posts
class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-date_posted")

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False




# Side bar content views
# Latest Posts
class LatestPostListView(ListView):
    model = Post
    template_name = "blog/post_latest.html"
    context_object_name = "posts"
    ordering = ["date_posted"]
    paginate_by = 5

# Older Posts
class OlderPostListView(ListView):
    model = Post
    template_name = "blog/post_older.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 5




# Announcements
class AnnouncementListView(ListView):
    model = Announcement
    template_name = "blog/announcements.html"
    context_object_name = "announcements"
    ordering = ["-date_posted"]
    paginate_by = 2

class UserAnnouncementListView(ListView):
    model = Announcement
    template_name = "blog/user_announcements.html"
    context_object_name = "announcements"
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get("username"))
        return Announcement.objects.filter(author=user).order_by("-date_posted")

class AnnouncementCreateView(LoginRequiredMixin, CreateView):
    model = Announcement
    fields = ["title", "content"]
    success_url = "/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AnnouncementDetailView(DetailView):
    model = Announcement

class AnnouncementUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Announcement
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        announcement = self.get_object()
        if self.request.user == announcement.author:
            return True
        return False

class AnnouncementDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Announcement
    success_url = "/"

    def test_func(self):
        announcement = self.get_object()
        if self.request.user == announcement.author:
            return True
        return False

def about(request):
    return render(request=request, template_name="blog/about.html", context={"title": "Custom Title"})