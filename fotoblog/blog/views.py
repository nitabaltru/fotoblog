from blog.forms import PhotoForm
from blog.models import Photo
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import View


@login_required
def home(request):
    photos = Photo.objects.all()
    return render(request, "blog/home.html", context={"photos": photos})


class PhotoUploadPage(View):
    template_name = "blog/photo_upload.html"
    form_class = PhotoForm

    def get(self, request):
        form = self.form_class()
        return render(
            request,
            self.template_name,
            context={"form": form},
        )

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            return redirect("home")
        return render(
            request,
            self.template_name,
            context={"form": form},
        )

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PhotoUploadPage, self).dispatch(request, *args, **kwargs)
