from django.db import models

# Create your models here. after creating a model or updating a model, you must makemigrations and migrate. remember to register it as well in admin.py in the same folder.
class BlogProject(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_date = models.DateField()
    blog_description = models.TextField()
