from authentication.forms import SignupForm, UploadProfilePhotoForm
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import View


class SignupPage(View):
    template_name = "authentication/signup.html"
    form_class = SignupForm

    def get(self, request):
        form = self.form_class()
        return render(
            request,
            self.template_name,
            context={"form": form},
        )

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        return render(
            request,
            self.template_name,
            context={"form": form},
        )


class UploadProfilePhotoPage(View):
    template_name = "authentication/upload_profile_photo.html"
    form_class = UploadProfilePhotoForm

    def get(self, request):
        form = self.form_class(instance=request.user)
        return render(
            request,
            self.template_name,
            context={"form": form},
        )

    def post(self, request):
        form = self.form_class(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("home")
        return render(
            request,
            self.template_name,
            context={"form": form},
        )

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UploadProfilePhotoPage, self).dispatch(request, *args, **kwargs)
