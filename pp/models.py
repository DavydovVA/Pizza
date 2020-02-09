from time import time
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from os.path import join, dirname, basename
from pp.utils import TimeAgo
from random import randint
import transliterate


class Post(models.Model):
    title = models.CharField(max_length=256, db_index=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def custom_save(self, *args, **kwargs):
        title = transliterate.translit(self.title.lower(), reversed=True)
        self.slug = slugify(title.replace(' ', '_').replace('-', '_')) + str(int(time()) + randint(1, 100))

        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title.lower().replace(' ', '_').replace('-', '_')) + str(
                int(time()) + randint(1, 100))

        super().save(*args, **kwargs)

    def __str__(self):
        return f'<{self.__class__.__name__}:{self.title}>'

    def get_created_at(self):
        return TimeAgo.get_time_ago(self.created_at)

    @staticmethod
    def upload_to(instance, filename):
        return join(
            dirname(basename(__file__)), instance.__class__.__name__, filename
        )


class Pizza(Post):
    body = models.TextField(blank=True, db_index=True)
    price = models.TextField(blank=True, default=None)
    image = models.ImageField(default=None, upload_to=Post.upload_to)

    def get_absolute_url(self):
        return reverse('pp:pizza', kwargs={'slug': self.slug})
