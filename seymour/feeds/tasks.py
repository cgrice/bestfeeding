import requests
from dateutil.parser import parse as parse_date
from datetime import datetime, timedelta
from celery.task import Task

from django.utils import timezone

class TaskFetchFeed(Task):

    name = 'feed-fetch'
    
    def run(self, feed, **kwargs):
        headers = {}
        if feed.etag != None:
            headers['If-None-Match'] = feed.etag
        if feed.last_modified != None:
            last_modified = feed.last_modified.strftime(
                '%A, %d-%B-%Y %H:%I:%S %Z' 
            )
            headers['If-Modified-Since'] = last_modified

        print "Getting latest feed for " + feed.feed_url

        r = requests.get(feed.feed_url, headers=headers)

        print "Status returned : %s" % r.status_code

        if r.status_code == 200:
            if 'ETag' in r.headers:
                feed.etag = r.headers['ETag']
            if 'Last-Modified' in r.headers:
                last_modified = parse_date(r.headers['Last-Modified'])
                feed.last_modified = last_modified
            feed.content = r.text
            feed.fetch_next = timezone.now() + timedelta(minutes=5)
        
        feed.parse()
        feed.save()
        
        print "Feed parsed and saved"        
        
        
