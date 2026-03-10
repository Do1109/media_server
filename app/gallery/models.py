from django.db import models
from django.contrib.auth.models import User


def upload_to(instance, filename: str) -> str:
    # uploads/photos/2026/03/xxx.jpg みたいに分けると運用が楽
    from datetime import datetime
    now = datetime.now()
    base = "photos" if instance.media_type == "photo" else "videos"
    return f"{base}/{now:%Y}/{now:%m}/{filename}"


def thumb_upload_to(instance, filename: str) -> str:
    from datetime import datetime
    now = datetime.now()
    return f"thumbs/{now:%Y}/{now:%m}/{filename}"


class MediaFile(models.Model):
    MEDIA_TYPE_CHOICES = (("photo", "Photo"), ("video", "Video"),
                          ("demo_sound", "Demo_Sound"),
                          ("sound_source,", "Sound_Source"))

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    media_type = models.CharField(max_length=20, choices=MEDIA_TYPE_CHOICES)
    file = models.FileField(upload_to=upload_to)
    title = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to="thumbs/", blank=True, null=True)

    def __str__(self):
        return f"{self.media_type}:{self.file.name}"


class InfoText(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField("本文")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.owner.username} - {self.created_at:%Y-%m-%d %H:%M}"
