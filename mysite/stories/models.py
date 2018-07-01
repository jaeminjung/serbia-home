from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Story(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(blank=True)
    author = models.ForeignKey(User, default=None)

    def __str__(self):
        return self.title

    def snippet(self):
        if len(self.body) < 50:
            return self.body
        else:
            return self.body[:50] + "    ..."


class Comment(models.Model):
    story = models.ForeignKey('Story', related_name='comment')
    author = models.ForeignKey(User, default=None)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    approve_comment = models.BooleanField(default=False)

    def approve(self):
        self.approve_comment = True
        self.save()

    def __str__(self):
        return self.text
