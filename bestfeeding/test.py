from feeds.models import Feed
feeds = Feed.objects.all()
for feed in feeds:
	feed.start_time = feed.round_time(feed.start_time, 15)
	feed.save()
