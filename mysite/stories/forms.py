from django import forms
from . import models


class CreateStory(forms.ModelForm):
    class Meta:
        model = models.Story
        fields = ['title', 'body', 'thumb']


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('text', )

