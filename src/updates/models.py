from django.conf import settings
from django.db import models
from django.core.serializers import serialize
import json
# Create your models here.


def upload_update_image(instance, filename):
    return "update/{user}/{filename}".format(user=instance.user, filename=filename)


class UpdateQuerySet(models.QuerySet):
    # def serialize(self):
        # qs = self
        # return serialize('json', qs, fields=("user", "content"))

    def serialize(self):
        qs = self
        list_values = list(self.values("user", "content", "image"))
        return list_values
        # final_array = []
        # for obj in qs:
        #     struct = json.loads(obj.serialize())
        #     final_array.append(struct)
        # return json.dumps(final_array)


class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model, using=self._db)


class Updates(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_update_image, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = UpdateManager()

    def __str__(self):
        return self.content or ""

    def serialize(self):
        try:
            image = self.image.url
        except:
            image = ""
        data = {
            "user": self.user.id,
            "content": self.content,
            "image": image

        }
        data = json.dumps(data)
        print(data)
        return data



        # json_data = serialize("json", [self], fields=("user", "content"))
        # struct = json.loads(json_data)
        # print(struct)
        # data = json.dumps(struct[0]["fields"])
        # return data



