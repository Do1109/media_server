from django.urls import path
from . import views

urlpatterns = [
    path("", views.media_list, name="media_list"),
    path("upload/", views.upload_media, name="upload_media"),
    path("m/<int:pk>/", views.media_detail, name="media_detail"),
    path("delete/<int:pk>/", views.delete_media, name="delete_media"),
    path("info/", views.band_info, name="band_info"),
    path("info/delete/<int:pk>/", views.delete_info, name="delete_info"),
    path("info/edit/<int:pk>/", views.edit_info, name="edit_info"),
]
