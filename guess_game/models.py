from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

class Book(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField(max)
    page_count = models.IntegerField(max)
    price = models.IntegerField(max)
    author = models.CharField(max_length=60)
    make_name = models.ForeignKey(Author, on_delete=models.CASCADE)







#
#
#
#
#
#                             ---
#                           /~~~~~\
#                          | `o o` |
#                           \ <_> /
#                             \ /
#                              |
#
#
#
#
#
#
#
#
#
