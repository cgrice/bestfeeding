from django.db import models
from django.contrib.auth.models import User
from feeds.models import Feed, Page

# Create your models here.
class UserSubscription(models.Model):
	user = models.ForeignKey(User)
	feed = models.ForeignKey(Feed)

	class Meta:
		unique_together = ("user", "feed")

class UserPage(models.Model):
	user = models.ForeignKey(User)
	page = models.ForeignKey(Page)
	read_date = models.DateTimeField()

	class Meta:
		unique_together = ("user", "page")
