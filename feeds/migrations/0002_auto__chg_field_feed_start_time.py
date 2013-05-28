# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Feed.start_time'
        db.alter_column(u'feeds_feed', 'start_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

    def backwards(self, orm):

        # Changing field 'Feed.start_time'
        db.alter_column(u'feeds_feed', 'start_time', self.gf('django.db.models.fields.DateTimeField')())

    models = {
        u'feeds.feed': {
            'Meta': {'object_name': 'Feed'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shield': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'side': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['feeds']