import json
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class PostQuerySet(models.QuerySet):
    def serialize(self):
        qs = self
        list_values = list(self.values("id", "author", "title", "content"))
        print("Queryset called", list_values)
        return json.dumps(list_values)


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, null=True)
    content = models.TextField(blank=True, null=True)

    objects = PostManager()



    def __str__(self):
        return self.content

    def serialize(self):
        data = {
            "id": self.id,
            "author": self.author.id,
            "title": self.title,
            "content": self.content
        }
        data = json.dumps(data)
        print("model function serializer ", data)
        return data
