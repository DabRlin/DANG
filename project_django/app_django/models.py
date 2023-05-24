from django.db import models

# Create your models here.
class MyModel(models.Model):
    # 模型字段和关系定义
    pass
class MyModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
