# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Feed.hour'
        db.alter_column(u'feeds_feed', 'hour', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Feed.day'
        db.alter_column(u'feeds_feed', 'day', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Feed.day_of_week'
        db.alter_column(u'feeds_feed', 'day_of_week', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Feed.month'
        db.alter_column(u'feeds_feed', 'month', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Feed.year'
        db.alter_column(u'feeds_feed', 'year', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Feed.minute'
        db.alter_column(u'feeds_feed', 'minute', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Feed.hour'
        raise RuntimeError("Cannot reverse this migration. 'Feed.hour' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Feed.day'
        raise RuntimeError("Cannot reverse this migration. 'Feed.day' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Feed.day_of_week'
        raise RuntimeError("Cannot reverse this migration. 'Feed.day_of_week' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Feed.month'
        raise RuntimeError("Cannot reverse this migration. 'Feed.month' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Feed.year'
        raise RuntimeError("Cannot reverse this migration. 'Feed.year' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Feed.minute'
        raise RuntimeError("Cannot reverse this migration. 'Feed.minute' and its values cannot be restored.")

    models = {
        u'feeds.feed': {
            'Meta': {'object_name': 'Feed'},
            'day': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'day_of_week': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'hour': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'month': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'shield': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'side': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        }
    }

    complete_apps = ['feeds']