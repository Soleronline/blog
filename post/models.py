from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(null=False, blank=False)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    comment = models.TextField(null=False, blank=False)
