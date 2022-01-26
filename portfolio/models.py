from django.db import models

"""
- create your models here. this file creates our database using model field types. see the Django model documentation for all types of fields.
- you must migrate this database after structuring it. see notion docs for detailed steps.
"""

class Project(models.Model):
    title = models.CharField(max_length=100) # set max character length
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='portfolio/images/') # uploaded to images folder inside portfolio app folder
    url = models.URLField(blank=True)
    href = models.CharField(blank=True, max_length=100)
