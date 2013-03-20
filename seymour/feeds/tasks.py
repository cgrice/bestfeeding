import requests
from dateutil.parser import parse as parse_date
from celery.task import Task

from .models import Feed

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
        r = requests.get(feed.feed_url, headers=headers)

        print r.request.headers

        if r.status_code == 200:
           if 'ETag' in r.headers:
                feed.etag = r.headers['ETag']
           if 'Last-Modified' in r.headers:
                last_modified = parse_date(r.headers['Last-Modified'])
                feed.last_modified = last_modified

        feed.save()

        print r.status_code
        
        
