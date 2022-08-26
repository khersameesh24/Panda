from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    LatestPostListView,
    OlderPostListView,
    AnnouncementListView,
    AnnouncementCreateView,
    AnnouncementDetailView,
    UserAnnouncementListView,
    AnnouncementUpdateView,
    AnnouncementDeleteView,
)
from . import views

urlpatterns = [

    # home page
    path("", view=PostListView.as_view(), name="blog-home"),

    # blog posts
    path("user/<str:username>", view=UserPostListView.as_view(), name="user-posts"),
    path("post/<int:pk>/", view=PostDetailView.as_view(), name="post-detail"),
    path("post/new/", view=PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update", view=PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete", view=PostDeleteView.as_view(), name="post-delete"),

    # latest-posts
    path("latestpost/", view=LatestPostListView.as_view(), name="latest-posts"),

    # older-posts
    path("olderpost/", view=OlderPostListView.as_view(), name="older-posts"),

    # announcements
    path("announcement/<str:username>", view=UserAnnouncementListView.as_view(), name="user-announcements"),
    path("announcement/<int:pk>/", view=AnnouncementDetailView.as_view(), name="announcement-detail"),
    path("announcement/new/", view=AnnouncementCreateView.as_view(), name="announcement-create"),
    path("announcements/", view=AnnouncementListView.as_view(), name="announcements"),
    path("announcement/<int:pk>/update", view=AnnouncementUpdateView.as_view(), name="announcement-update"),
    path("announcement/<int:pk>/delete", view=AnnouncementDeleteView.as_view(), name="announcement-delete"),

    # about page
    path("about/", view=views.about, name="blog-about"),
]
