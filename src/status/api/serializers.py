from rest_framework import serializers
from status.models import Status


# serializers -> JSON
# serializers -> validate data


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id','user', 'content', 'image']
        read_only_fields = ['user']  #GET

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


