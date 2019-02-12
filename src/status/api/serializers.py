from rest_framework import serializers
from status.models import Status
from accounts.api.serializers import UserPublicSerializer


# serializers -> JSON
# serializers -> validate data


class StatusInlineUserSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Status
        fields = ['uri', 'id', 'content', 'image']

    def get_uri(self, obj):
        return "/api/status/{id}".format(id=obj.id)


class StatusSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Status
        fields = ['uri', 'id', 'user', 'content', 'image', ]
        read_only_fields = ['user']  # GET

    def get_uri(self, obj):
        return "/api/users/{id}/".format(id=obj.id)

    # def validate_content(self, value):
    #     if len(value) > 10000:
    #         raise serializers.ValidationError("This is way too long")
    #     return value

    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if image is None and content is None:
            raise serializers.ValidationError("Content or Image is required.")
        return data
