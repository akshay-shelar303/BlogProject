from django.db import models


class Auther(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ThreadPost(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    likes = models.IntegerField()
    created_at = models.DateTimeField("D/M/Y:T")

    def __str__(self):
        return f"{self.title}"
