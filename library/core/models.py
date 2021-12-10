from django.db import models

from library.util import rename_imagefile_to_uuid

# Create your models here.


class Book(models.Model):

    book_name = models.CharField(max_length=120, null=False)
    ISBN = models.CharField(max_length=100, null=False)
    page = models.IntegerField(default=0, null=False)
    publication_date = models.DateField(null=False)
    publisher = models.CharField(max_length=60, null=False)
    author = models.CharField(max_length=20, null=False)
    image = models.ImageField(null=False, upload_to=rename_imagefile_to_uuid)

    def __str__(self):
        return self.book_name
