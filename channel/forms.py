from django import forms
from .models import Channel


class PostForm(forms.ModelForm):
    class Meta:
        model = Channel
        fields = ('post_img', 'post_header', 'post_content')