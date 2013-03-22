# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Page'
        db.create_table(u'feeds_page', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feed', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['feeds.Feed'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('original_content', self.gf('django.db.models.fields.TextField')()),
            ('content_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('author_name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('permalink', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('guid', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('hash', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'feeds', ['Page'])


    def backwards(self, orm):
        # Deleting model 'Page'
        db.delete_table(u'feeds_page')


    models = {
        u'feeds.feed': {
            'Meta': {'object_name': 'Feed'},
            'etag': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'feed_url': ('django.db.models.fields.URLField', [], {'max_length': '512'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'feeds.page': {
            'Meta': {'object_name': 'Page'},
            'author_name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feeds.Feed']"}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'hash': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original_content': ('django.db.models.fields.TextField', [], {}),
            'permalink': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['feeds']