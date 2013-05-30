from feeds.models import Feed
feeds = Feed.objects.all()
for feed in feeds:
    feed.year = feed.start_time.year
    feed.month = feed.start_time.month
    feed.day = feed.start_time.day
    feed.day_of_week = feed.start_time.weekday()
    feed.minute = feed.start_time.minute
    feed.hour = feed.start_time.hour
    feed.save()
