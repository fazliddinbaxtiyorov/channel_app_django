from django.db import models
from django.utils import timezone


class Channel(models.Model):
    post_img = models.ImageField(upload_to='images/', blank=True)
    post_header = models.CharField(max_length=100)
    post_content = models.TextField(max_length=440)
    post_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.post_header
