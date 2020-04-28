from django.db import models


class Post(models.Model):
    objects = models.Manager()  # class has no objects member오류 때문에 집어넣음
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
