from django.db import models

# Create your models here.
class Anime(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    desc = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=222)

    def __str__(self):
        return self.name