from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(u'Title', max_length=50)
    text = models.TextField(u'Text', max_length=1000)
    url = models.URLField(u'Link', max_length=300)