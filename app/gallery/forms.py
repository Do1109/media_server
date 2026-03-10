from django import forms
from .models import MediaFile
from .models import InfoText


class MediaUploadForm(forms.ModelForm):
    class Meta:
        model = MediaFile
        fields = ["media_type", "file", "title"]
        widgets = {
            "media_type": forms.Select(attrs={"class": "form-select"}),
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "タイトルを入力"
                }
            ),
            "file": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }


class InfoTextForm(forms.ModelForm):
    class Meta:
        model = InfoText
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "メッセージを書く..."
            }),
        }
