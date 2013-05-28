"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""


from django.test import TestCase

from .models import Feed

import datetime


class FeedTest(TestCase):

    time_00 = datetime.datetime(day=1, month=1, year=2013, hour=12, minute=0, second=0)
    time_15 = datetime.datetime(day=1, month=1, year=2013, hour=12, minute=15, second=0)
    time_30 = datetime.datetime(day=1, month=1, year=2013, hour=12, minute=30, second=0)
    time_45 = datetime.datetime(day=1, month=1, year=2013, hour=12, minute=45, second=0)
    time_nexthour = datetime.datetime(day=1, month=1, year=2013, hour=13, minute=0, second=0)

    def test_exact_round_times(self):
        feed = Feed()
        self.assertEqual(feed.round_time(self.time_00, 15), self.time_00)
        self.assertEqual(feed.round_time(self.time_15, 15), self.time_15)
        self.assertEqual(feed.round_time(self.time_30, 15), self.time_30)
        self.assertEqual(feed.round_time(self.time_45, 15), self.time_45)

    def test_round_time(self):
        feed = Feed()

        time_05 = datetime.datetime(day=1, month=1, year=2013, hour=12, minute=5, second=0)
        time_10 = datetime.datetime(day=1, month=1, year=2013, hour=12, minute=10, second=0)
        time_20 = datetime.datetime(day=1, month=1, year=2013, hour=12, minute=20, second=0)
        time_25 = datetime.datetime(day=1, month=1, year=2013, hour=12, minute=25, second=0)
        time_35 = datetime.datetime(day=1, month=1, year=2013, hour=12, minute=35, second=0)
        time_40 = datetime.datetime(day=1, month=1, year=2013, hour=12, minute=40, second=0)
        time_50 = datetime.datetime(day=1, month=1, year=2013, hour=12, minute=50, second=0)
        time_55 = datetime.datetime(day=1, month=1, year=2013, hour=12, minute=55, second=0)

        self.assertEqual(feed.round_time(time_05, 15), self.time_00)
        self.assertEqual(feed.round_time(time_10, 15), self.time_15)
        self.assertEqual(feed.round_time(time_20, 15), self.time_15)
        self.assertEqual(feed.round_time(time_25, 15), self.time_30)
        self.assertEqual(feed.round_time(time_35, 15), self.time_30)
        self.assertEqual(feed.round_time(time_40, 15), self.time_45)
        self.assertEqual(feed.round_time(time_50, 15), self.time_45)
        self.assertEqual(feed.round_time(time_55, 15), self.time_nexthour)

    def test_next_days(self):
        feed = Feed()

        time_55 = datetime.datetime(day=1, month=1, year=2013, hour=23, minute=55, second=0)
        time_05 = datetime.datetime(day=2, month=1, year=2013, hour=0, minute=5, second=0)
        time_nextday = datetime.datetime(day=2, month=1, year=2013, hour=0, minute=0, second=0)
        time_prevday = datetime.datetime(day=2, month=1, year=2013, hour=0, minute=0, second=0)

        self.assertEqual(feed.round_time(time_55, 15), time_nextday)
        self.assertEqual(feed.round_time(time_05, 15), time_prevday)

    def test_next_year(self):
        feed = Feed()

        time_55 = datetime.datetime(day=31, month=12, year=2012, hour=23, minute=55, second=0)
        time_nextday = datetime.datetime(day=1, month=1, year=2013, hour=0, minute=0, second=0)

        self.assertEqual(feed.round_time(time_55, 15), time_nextday)

    def test_repeat_round(self):
        feed = Feed()

        time_25 = datetime.datetime(day=1, month=1, year=2013, hour=12, minute=25, second=0)

        result_time = feed.round_time(time_25, 15)

        self.assertEqual(result_time, self.time_30)

        result_time = feed.round_time(result_time, 15)
        
        self.assertEqual(result_time, self.time_30)

