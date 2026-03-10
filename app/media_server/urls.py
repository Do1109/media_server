from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    # ログイン/ログアウト（Django標準）
    path("login/", auth_views.LoginView.as_view(template_name="gallery/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # トップを gallery に
    path("", include("gallery.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)