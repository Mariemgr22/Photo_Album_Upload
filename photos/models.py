from django.db import models
import os
from django.urls import reverse

class Photo(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', default="uploads/default.jpg")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def filename(self):
        if self.image:
            return os.path.basename(self.image.name)
        return "No Image"

    def get_image_url(self):
        if self.image:
            return self.image.url
        return ""

    def get_absolute_url(self):
        return reverse('photo-retrieve-update-destroy', kwargs={'pk': self.pk})

    def __str__(self):
        return self.filename()