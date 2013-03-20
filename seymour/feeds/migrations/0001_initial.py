# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Feed'
        db.create_table(u'feeds_feed', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feed_url', self.gf('django.db.models.fields.URLField')(max_length=512)),
            ('etag', self.gf('django.db.models.fields.TextField')(null=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(null=True)),
        ))
        db.send_create_signal(u'feeds', ['Feed'])


    def backwards(self, orm):
        # Deleting model 'Feed'
        db.delete_table(u'feeds_feed')


    models = {
        u'feeds.feed': {
            'Meta': {'object_name': 'Feed'},
            'etag': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'feed_url': ('django.db.models.fields.URLField', [], {'max_length': '512'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        }
    }

    complete_apps = ['feeds']