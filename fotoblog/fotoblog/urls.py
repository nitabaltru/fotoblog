"""fotoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from authentication.views import SignupPage, UploadProfilePhotoPage
from blog.views import PhotoUploadPage, home
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeDoneView,
    PasswordChangeView,
)
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    # blog
    path("home/", home, name="home"),
    path(
        "photo/upload/",
        PhotoUploadPage.as_view(),
        name="photo_upload",
    ),
    # auth
    path(
        "signup/",
        SignupPage.as_view(),
        name="signup",
    ),
    path(
        "",
        LoginView.as_view(
            template_name="authentication/login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(
            next_page="login",
        ),
        name="logout",
    ),
    path(
        "change-password/",
        PasswordChangeView.as_view(
            template_name="authentication/password_change_form.html"
        ),
        name="password_change",
    ),
    path(
        "change-password-done/",
        PasswordChangeDoneView.as_view(
            template_name="authentication/password_change_done.html"
        ),
        name="password_change_done",
    ),
    path(
        "change-profile-photo/",
        UploadProfilePhotoPage.as_view(),
        name="change_profile_photo",
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
