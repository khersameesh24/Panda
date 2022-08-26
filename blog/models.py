from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=2500)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title} from {self.author}"

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

class Announcement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    date_posted = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} announcement"

    def get_absolute_url(self):
        return reverse("announcement-detail", kwargs={"pk": self.pk})
    