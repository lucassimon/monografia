# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Contact.person'
        db.add_column(u'api_contact', 'person',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='contacts', to=orm['api.Person']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Contact.person'
        db.delete_column(u'api_contact', 'person_id')


    models = {
        u'api.contact': {
            'Meta': {'ordering': "['created']", 'object_name': 'Contact'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contacts'", 'to': u"orm['api.Person']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.person': {
            'Meta': {'ordering': "['created']", 'object_name': 'Person'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['api']