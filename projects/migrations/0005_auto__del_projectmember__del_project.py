# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ProjectMember'
        db.delete_table('projects_projectmember')

        # Deleting model 'Project'
        db.delete_table('projects_project')


    def backwards(self, orm):
        # Adding model 'ProjectMember'
        db.create_table('projects_projectmember', (
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='member', to=orm['projects.Project'])),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Roles'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='member_in_projects', to=orm['auth.User'])),
        ))
        db.send_create_signal('projects', ['ProjectMember'])

        # Adding model 'Project'
        db.create_table('projects_project', (
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('projects', ['Project'])


    models = {
        'projects.roles': {
            'Meta': {'object_name': 'Roles'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['projects']