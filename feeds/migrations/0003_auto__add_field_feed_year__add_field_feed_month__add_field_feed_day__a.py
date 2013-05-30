# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Feed.year'
        db.add_column(u'feeds_feed', 'year',
                      self.gf('django.db.models.fields.IntegerField')(default=2013, blank=True),
                      keep_default=False)

        # Adding field 'Feed.month'
        db.add_column(u'feeds_feed', 'month',
                      self.gf('django.db.models.fields.IntegerField')(default=5, blank=True),
                      keep_default=False)

        # Adding field 'Feed.day'
        db.add_column(u'feeds_feed', 'day',
                      self.gf('django.db.models.fields.IntegerField')(default=30, blank=True),
                      keep_default=False)

        # Adding field 'Feed.day_of_week'
        db.add_column(u'feeds_feed', 'day_of_week',
                      self.gf('django.db.models.fields.IntegerField')(default=1, blank=True),
                      keep_default=False)

        # Adding field 'Feed.hour'
        db.add_column(u'feeds_feed', 'hour',
                      self.gf('django.db.models.fields.IntegerField')(default=1, blank=True),
                      keep_default=False)

        # Adding field 'Feed.minute'
        db.add_column(u'feeds_feed', 'minute',
                      self.gf('django.db.models.fields.IntegerField')(default=1, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Feed.year'
        db.delete_column(u'feeds_feed', 'year')

        # Deleting field 'Feed.month'
        db.delete_column(u'feeds_feed', 'month')

        # Deleting field 'Feed.day'
        db.delete_column(u'feeds_feed', 'day')

        # Deleting field 'Feed.day_of_week'
        db.delete_column(u'feeds_feed', 'day_of_week')

        # Deleting field 'Feed.hour'
        db.delete_column(u'feeds_feed', 'hour')

        # Deleting field 'Feed.minute'
        db.delete_column(u'feeds_feed', 'minute')


    models = {
        u'feeds.feed': {
            'Meta': {'object_name': 'Feed'},
            'day': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'day_of_week': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'hour': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'month': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'shield': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'side': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['feeds']