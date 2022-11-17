from blog.forms import BlogForm, PhotoForm
from blog.models import Blog, Photo
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, View


@login_required
def home(request):
    photos = Photo.objects.all()
    blogs = Blog.objects.all()
    return render(request, "blog/home.html", context={"photos": photos, "blogs": blogs})


class BlogDetail(DetailView):
    model = Blog
    template_name = "blog/view_blog.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(BlogDetail, self).dispatch(request, *args, **kwargs)


class BlogAndPhotoUpload(View):
    template_name = "blog/create_blog_post.html"
    blog_form_class = BlogForm
    photo_form_class = PhotoForm

    def get(self, request):
        blog_form = self.blog_form_class()
        photo_form = self.photo_form_class()
        return render(
            request,
            self.template_name,
            context={
                "blog_form": blog_form,
                "photo_form": photo_form,
            },
        )

    def post(self, request):
        blog_form = self.blog_form_class(request.POST)
        photo_form = self.photo_form_class(request.POST, request.FILES)
        if all([blog_form.is_valid(), photo_form.is_valid()]):
            # photo
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            # blog
            blog = blog_form.save(commit=False)
            blog.author = request.user
            blog.photo = photo
            blog.save()
            return redirect("home")
        return render(
            request,
            self.template_name,
            context={
                "blog_form": blog_form,
                "photo_form": photo_form,
            },
        )

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(BlogAndPhotoUpload, self).dispatch(request, *args, **kwargs)


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
