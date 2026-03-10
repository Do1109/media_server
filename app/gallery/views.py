from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import MediaFile
from .forms import MediaUploadForm
from .models import InfoText
from .forms import InfoTextForm
from PIL import Image
from django.core.files.base import ContentFile
from io import BytesIO
import os
import subprocess


@login_required
def media_list(request):
    qs = MediaFile.objects.filter(owner=request.user)

    sort = request.GET.get("sort", "new")
    year = request.GET.get("year", "")

    if year:
        qs = qs.filter(uploaded_at__year=year)

    if sort == "old":
        qs = qs.order_by("uploaded_at")
    else:
        qs = qs.order_by("-uploaded_at")

    years = (
        MediaFile.objects.filter(owner=request.user)
        .dates("uploaded_at", "year", order="DESC")
    )

    return render(
        request,
        "gallery/list.html",
        {
            "files": qs,
            "sort": sort,
            "selected_year": year,
            "years": years,
        },
    )


@login_required
def upload_media(request):
    if request.method == "POST":
        form = MediaUploadForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()

            if obj.media_type == "photo":
                img = Image.open(obj.file.path)
                img = img.convert("RGB")
                img.thumbnail((400, 400))

                buf = BytesIO()
                img.save(buf, format="JPEG", quality=85)
                buf.seek(0)

            base, _ = os.path.splitext(os.path.basename(obj.file.name))
            thumb_name = f"{base}_thumb.jpg"

            obj.thumbnail.save(thumb_name, ContentFile(buf.read()), save=True)

        elif obj.media_type == "video":

            base, _ = os.path.splitext(os.path.basename(obj.file.name))
            thumb_name = f"{base}_thumb.jpg"

            thumb_dir = os.path.join(os.path.dirname(obj.file.path), "..", "..", "thumbs")
            thumb_dir = os.path.abspath(thumb_dir)
            os.makedirs(thumb_dir, exist_ok=True)

            thumb_path = os.path.join(thumb_dir, thumb_name)

            command = [
                    "ffmpeg",
                    "-i", obj.file.path,
                    "-ss", "00:00:01",
                    "-vframes", "1",
                    thumb_path,
                    "-y"
                ]
            subprocess.run(command, check=True)

            relative_thumb_path = os.path.relpath(thumb_path, obj.file.storage.location)
            obj.thumbnail.name = relative_thumb_path.replace("\\", "/")
            obj.save()

            return redirect("media_list")
    else:
        form = MediaUploadForm()

    return render(request, "gallery/upload.html", {"form": form})


@login_required
def media_detail(request, pk: int):
    obj = get_object_or_404(MediaFile, pk=pk, owner=request.user)
    return render(request, "gallery/detail.html", {"obj": obj})


@login_required
def band_info(request):
    if request.method == "POST":
        form = InfoTextForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()
            return redirect("band_info")
    else:
        form = InfoTextForm()

    posts = InfoText.objects.order_by("-created_at")

    return render(request, "gallery/info.html", {
        "form": form,
        "posts": posts
    })


@login_required
def delete_media(request, pk: int):
    obj = get_object_or_404(MediaFile, pk=pk, owner=request.user)

    if request.method == "POST":
        if obj.file:
            obj.file.delete(save=False)
        if obj.thumbnail:
            obj.thumbnail.delete(save=False)
        obj.delete()
        return redirect("media_list")

    return render(request, "gallery/delete_confirm.html", {"obj": obj})
