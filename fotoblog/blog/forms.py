from blog.models import Photo
from django.forms import ModelForm


class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ["image", "caption"]
