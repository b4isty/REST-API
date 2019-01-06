from django.conf import settings
from django.db import models

# Create your models here.


def upload_update_image(instance, filename):
    return "update/{user}/{filename}".format(user=instance.user, filename=filename)


class Updates(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_update_image, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content or ""




