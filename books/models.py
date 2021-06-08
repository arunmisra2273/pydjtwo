from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=256)
    pageCount = models.IntegerField(default=0)
    thumbnailUrl = models.CharField(max_length=256, null=True)
    shortDescription = models.TextField(null=True)
    longDescription = models.TextField(null=True)

    def __str__(self) -> str:
        return f"{self.id}  {self.title}"

class Review(models.Model):
    body = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    book_id = models.BigIntegerField()

    def __str__(self) -> str:
        return f"{self.id}  {self.body}"
