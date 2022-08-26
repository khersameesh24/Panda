from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    """
    User profile model
    The user profile has a one to one relationship with the
    User auth model
    Deletes a user profile if the corresponding user is deleted
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_sise = (300, 300)
            img.thumbnail(output_sise)
            img.save(self.image.path)


