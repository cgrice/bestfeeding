from feeds.tasks import TaskFetchFeed
from feeds.models import Feed
feed = Feed.objects.get(pk=1)
TaskFetchFeed.delay(feed)
