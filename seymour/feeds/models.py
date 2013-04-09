from django.db import models
from django.utils import timezone

import datetime

from dateutil.parser import parse as parse_date

from .tasks import TaskFetchFeed

# Create your models here.
class Feed(models.Model):

    feed_url = models.URLField(max_length=512)
    etag = models.TextField(null=True) 
    last_modified = models.DateTimeField(null=True)
    content = models.TextField(null=True)
    fetch_next = models.DateTimeField(null=True)

    def __unicode__(self):
        return self.feed_url

    def parse(self):
        from feedparser import parse as parse_feed
        if self.content:
            feed = parse_feed(self.content)
            for entry in feed.entries:   
                page = Page()
                page.title = entry.title
                page.date = parse_date(entry.published)
                page.feed = self
                page.permalink = entry.link
                page.guid = entry.id
                page.content = entry.description
                page.save()
        else:
            return False 

    def fetch(self):
        if self.fetch_next is None or self.fetch_next <= timezone.now():
            task = TaskFetchFeed()
            if(len(self.pages.all()) == 0):
                task.run(self)
            else:
                TaskFetchFeed.delay(self)


    def save(self, *args, **kwargs):
        if not self.fetch_next:
            self.fetch_next = timezone.now()

        try:
            super(Feed, self).save(*args, **kwargs)
        except e:
            raise e

class Page(models.Model):

    feed = models.ForeignKey('Feed', related_name="pages")
    date = models.DateTimeField()
    title = models.CharField(max_length=1024)
    content = models.TextField()
    original_content = models.TextField()
    content_type = models.CharField(max_length=255)
    author_name = models.CharField(max_length=1024)
    permalink = models.CharField(max_length=1024)
    guid = models.CharField(max_length=512)
    hash = models.CharField(max_length=128)

    def __unicode__(self):
        return "%s" % (self.title,)
