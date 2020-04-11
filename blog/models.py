from django.conf import settings
from django.db import models
from django.utils import timezone
from django.shortcuts import reverse


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=150, unique=True, default='')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
