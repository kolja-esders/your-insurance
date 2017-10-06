from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from custom_user.models import AbstractEmailUser

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    class Meta:
        unique_together = ('title', 'author')

    def __str__(self):
        return self.title + ' (' + self.author + ')'

class Group(models.Model):
    name = models.CharField(max_length=32, unique=True)
    name_url = models.CharField(max_length=64, unique=True)

    @staticmethod
    def get_url_from_name(name):
        return name.strip().lower().replace('.', '').replace(',', '').replace(' ', '-')

class CustomUser(AbstractEmailUser):
    username = models.CharField(max_length=31, blank=True)
    first_name = models.CharField(max_length=31, blank=True)
    last_name = models.CharField(max_length=31, blank=True)
    groups = models.ManyToManyField(Group, through='Membership', symmetrical=False, related_name='users')
    books = models.ManyToManyField(Book, through='BookshelfEntry', symmetrical=False, related_name='users')

class BookshelfEntry(models.Model):
    user = models.ForeignKey(CustomUser)
    book = models.ForeignKey(Book)
    state = models.CharField(max_length = 31) # to-read, read, ...
    rating = models.PositiveSmallIntegerField(null=True)

    class Meta:
        unique_together = ('user', 'book')

class Membership(models.Model):
    user = models.ForeignKey(CustomUser)
    group = models.ForeignKey(Group)

    class Meta:
        unique_together = ('user', 'group')
