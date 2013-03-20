from django.db import models

# Create your models here.
class Feed(models.Model):

    feed_url = models.URLField(max_length=512)
    etag = models.TextField(null=True) 
    last_modified = models.DateTimeField(null=True)

class Page(models.Model):

    feed = models.ForeignKey('Feed')
    date = models.DateTimeField()
    title = models.CharField(max_length=1024)
    content = models.TextField()
    original_content = models.TextField()
    content_type = models.CharField(max_length=255)
    author_name = models.CharField(max_length=1024)
    permalink = models.CharField(max_length=1024)
    guid = models.CharField(max_length=512)
    hash = models.CharField(max_length=128)
