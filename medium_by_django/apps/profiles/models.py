from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='medium_by_django/media/')
    followings = models.ManyToManyField(to='self', related_name='followers', symmetrical=False)

    def __str__(self):
        return self.user.username

    def follow(self, profile):
        self.followings.add(profile)

    def unfollow(self, profile):
        self.followings.remove(profile)

