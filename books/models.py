from django.db import models
from uuid import uuid4


def upload_image_book(instance, filename):
    return f"{instance.id_books}-{filename}"


class Books(models.Model):
    id_books = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=225)
    author = models.CharField(max_length=225)
    release_year = models.IntegerField()
    state = models.CharField(max_length=50)
    pages = models.IntegerField()
    publishing_company = models.CharField(max_length=225)
    creat_at = models.DateField(auto_now_add=True)
    image = models.ImageField(
        upload_to=upload_image_book, blank=True, null=True)
