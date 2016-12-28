from django import forms
from .models import Bloggg

class BlogggForm(forms.ModelForm):
    class Meta:
        model = Bloggg
        fields = ["title","parag","tags"]