from django.db import models
from dateutil.parser import parse as parse_date

# Create your models here.
class Feed(models.Model):

    feed_url = models.URLField(max_length=512)
    etag = models.TextField(null=True) 
    last_modified = models.DateTimeField(null=True)
    content = models.TextField(null=True)
    fetch_next = models.DateTimeField(null=True)

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
                print page
        else:
            return False 

    def fetch(self):
        task = TaskFetchFeed()
        if(len(feed.pages.all()) == 0):
            task.run(self)
        else:
            TaskFetchFeed.delay(self)

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
