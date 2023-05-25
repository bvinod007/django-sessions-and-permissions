from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Books(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    book_name = models.CharField(max_length=100)
    book_author = models.CharField(max_length=30)
    book_published_on_date = models.DateField()
    book_price = models.IntegerField()
    pages = models.IntegerField()
