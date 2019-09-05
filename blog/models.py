from django.db import models


class Squad(models.Model):
    name = models.CharField(max_length=100)


class User(models.Model):
    username = models.CharField(max_length=80)
    pass_hash = models.CharField(max_length=512)
    squad = models.ForeignKey(Squad, null=True, on_delete=models.SET_NULL)
    is_admin = models.BooleanField(default=False)


class Article(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=8192)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=8192)
