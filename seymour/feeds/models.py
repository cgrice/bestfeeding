from django.db import models

# Create your models here.
class Feed(models.Model):

    feed_url = models.URLField(max_length=512)
    etag = models.TextField(null=True) 
    last_modified = models.DateTimeField(null=True)
