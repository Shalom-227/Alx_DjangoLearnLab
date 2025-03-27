from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator


# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField(validators=[MinLengthValidator(5)], max_length = 150, help_text= "Tell people something about yourself")
    profile_picture = models.ImageField(upload_to="profile_pictures", null=True, blank=True)
    #No need for a separate followers field: Django automatically handles the reverse relation.
    following = models.ManyToManyField("self", symmetrical=False, related_name="followers", blank=True)

    def __str__(self):
        return self.username

