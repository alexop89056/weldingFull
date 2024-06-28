import random

from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Work(models.Model):
    slug = models.SlugField(max_length=100)
    short_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    main_img = models.ImageField(upload_to="work")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        base_slug = slugify(self.slug)[:50]
        random_num = random.randint(1000, 9999)
        unique_slug = f"{base_slug}-{random_num}"
        self.slug = unique_slug
        super().save(*args, **kwargs)
