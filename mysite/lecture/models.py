from django.db import models

# Create your models here.

class UploadFileModel(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(null=True)
    class_date = models.CharField(max_length=20, null=True)
    uploaded_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title