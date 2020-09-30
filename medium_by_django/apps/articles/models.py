from django.db import models
from medium_by_django.apps.profiles.models import Profile


class Tag(models.Model):
    # TODO: Why we have name??
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.slug


class Article(models.Model):
    slug = models.CharField(max_length=255, db_index=True, unique=True)
    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='articles')
    # TODO: what happends when we delete an object in many to many? cascade?
    Tags = models.ManyToManyField(to=Tag, related_name='articles')
    claps = models.ManyToManyField(to=Profile, related_name='claps')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug


class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.article) + str(self.pk)




