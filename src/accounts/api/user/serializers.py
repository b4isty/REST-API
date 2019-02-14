from django.contrib.auth import get_user_model
from rest_framework import serializers
from status.api.serializers import StatusInlineUserSerializer
from rest_framework.reverse import reverse as api_reverse

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    status = serializers.SerializerMethodField(read_only=True)

    # status_uri = serializers.SerializerMethodField(read_only=True)
    # recent_status = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "uri", "status"]

    def get_uri(self, obj):
        request = self.context.get("request")
        return api_reverse("api-user:detail", kwargs={"username": obj.username}, request=request)
        # return "/api/users/{id}/".format(id=obj.id)

    # def get_status_uri(self, obj):
    #     return self.get_uri(obj) + "status/"

    def get_status(self, obj):
        request = self.context.get("request")
        limit = 10
        if request:
            limit_query = request.GET.get("limit")
            try:
                limit = int(limit_query)
            except:
                pass
        qs = obj.status_set.all()
        data = {
            "uri": self.get_uri(obj) + "status/",
            "last": StatusInlineUserSerializer(qs.first(), context={"request": request}).data,
            "recent": StatusInlineUserSerializer(qs[:limit], many=True,  context={"request": request}).data
        }
        return data

    # def get_recent_status(self, obj):
    #     qs = obj.status_set.all().order_by("-timestamp")[:10]  # Status.objects.filter(user=obj)
    #     return StatusInlineUserSerializer(qs, many=True).data
