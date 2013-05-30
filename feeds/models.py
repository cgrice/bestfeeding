from django.db import models
from django.utils import timezone

import datetime

# Create your models here.
class Feed(models.Model):

	SIDE_CHOICES = (
		('L', 'Left'),
		('R', 'Right'),
	)
	
	start_time = models.DateTimeField(auto_now_add=True, blank=True)
    year = models.IntegerField(blank=True)
    month = models.IntegerField(blank=True)
    day = models.IntegerField(blank=True)
    day_of_week = models.IntegerField(blank=True)
    hour = models.IntegerField(blank=True)
    minute = models.IntegerField(blank=True)
	side = models.CharField(max_length=1,
				choices=SIDE_CHOICES)
	shield = models.BooleanField()

	def get_absolute_url(self):
		return '/'
	
	def round_time(self, time, round_to):
		"""Round a datetime object to any time laps in seconds
		dt : datetime.datetime object, default now.
		roundTo : Closest number of seconds to round to, default 1 minute.
		Author: Thierry Husson 2012 - Use it as you want but don't blame me.
		"""
		min_modulo = 60
		closest_to = 0

		for seconds in [15,30,45,60]:
			if time.minute % seconds < min_modulo or time.minute % seconds == min_modulo:
				min_modulo = time.minute % seconds
				closest_to = seconds

		if closest_to == 60 and time.minute < 50:
			closest_to = 0

		if time.minute < 7 and time.second < 30:
			time = time.replace(minute=0)
		elif time.minute - closest_to < closest_to + 15 - time.minute:
			if closest_to == 60:
				time = time.replace(hour=time.hour, minute=0)
				time = time + datetime.timedelta(hours=1)
			else:
				time = time.replace(minute=closest_to)
		else:
			if closest_to == 60:
				time = time.replace(hour=time.hour, minute=0)
				time = time + datetime.timedelta(hours=1)
			else: 
				time = time.replace(minute=closest_to)
				time = time + datetime.timedelta(minutes=15)

		time = time.replace(second=0, microsecond=0)
		return time
		
		
		
