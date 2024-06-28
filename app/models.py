from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Work(models.Model):
    short_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    main_img = models.ImageField(upload_to="work")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
