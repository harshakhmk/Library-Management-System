from django.db import models
from authentication.models import User
# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    def get_books(self):
        return Books.objects.filter(category=self)

class Books(models.Model):
    id = models.AutoField(primary_key=True)
    image_url = models.URLField()
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category_id = models.ForeignKey(Category,null=True, on_delete=models.SET_NULL)
    category = models.CharField(max_length=100)
    created_by_user_id = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)