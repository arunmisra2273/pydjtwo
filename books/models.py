from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Book(models.Model):
    title = models.CharField(max_length=256)
    pageCount = models.IntegerField(default=0)
    thumbnailUrl = models.CharField(max_length=256, null=True)
    shortDescription = models.TextField(null=True)
    longDescription = models.TextField(null=True)
    authors = models.ManyToManyField(Author)

    def __str__(self) -> str:
        return f"{self.id}  {self.title}"

class Review(models.Model):
    body = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book, on_delete=CASCADE, null=True)

    def __str__(self) -> str:
        return f"{self.id}  {self.body}"
