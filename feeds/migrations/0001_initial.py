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
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('side', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('shield', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'feeds', ['Feed'])


    def backwards(self, orm):
        # Deleting model 'Feed'
        db.delete_table(u'feeds_feed')


    models = {
        u'feeds.feed': {
            'Meta': {'object_name': 'Feed'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shield': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'side': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['feeds']