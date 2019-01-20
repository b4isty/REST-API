from django import forms

from .models import Updates


class UpdateModelForm(forms.ModelForm):
    class Meta:
        model = Updates
        fields = ["user", "content", "image"]

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise forms.ValidationError("Content or Image is required")

        return super().clean(*args, **kwargs)




