# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'BackLog'
        db.delete_table('projects_backlog')

        # Adding model 'ProductBacklog'
        db.create_table('projects_productbacklog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='project', to=orm['projects.Project'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('projects', ['ProductBacklog'])

        # Adding model 'SprintBackLog'
        db.create_table('projects_sprintbacklog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('sprint', self.gf('django.db.models.fields.related.ForeignKey')(related_name='backlog', to=orm['projects.Sprint'])),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sprint_backlogs', to=orm['projects.Project'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('projects', ['SprintBackLog'])

        # Adding model 'ProductBacklogTask'
        db.create_table('projects_productbacklogtask', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('backlog', self.gf('django.db.models.fields.related.ForeignKey')(related_name='backlog', to=orm['projects.ProductBacklog'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(max_length=1000)),
            ('estimate', self.gf('django.db.models.fields.FloatField')(max_length=1000)),
            ('demo_test', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('projects', ['ProductBacklogTask'])

        # Adding field 'ProjectMember.created_at'
        db.add_column('projects_projectmember', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=None, blank=True),
                      keep_default=False)

        # Adding field 'ProjectMember.updated_at'
        db.add_column('projects_projectmember', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=None, blank=True),
                      keep_default=False)

        # Adding field 'Project.created_at'
        db.add_column('projects_project', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=None, blank=True),
                      keep_default=False)

        # Adding field 'Project.updated_at'
        db.add_column('projects_project', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=None, blank=True),
                      keep_default=False)

        # Adding field 'SprintTask.created_at'
        db.add_column('projects_sprinttask', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=None, blank=True),
                      keep_default=False)

        # Adding field 'SprintTask.updated_at'
        db.add_column('projects_sprinttask', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=None, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'BackLog'
        db.create_table('projects_backlog', (
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='backlog_project', to=orm['projects.Project'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('projects', ['BackLog'])

        # Deleting model 'ProductBacklog'
        db.delete_table('projects_productbacklog')

        # Deleting model 'SprintBackLog'
        db.delete_table('projects_sprintbacklog')

        # Deleting model 'ProductBacklogTask'
        db.delete_table('projects_productbacklogtask')

        # Deleting field 'ProjectMember.created_at'
        db.delete_column('projects_projectmember', 'created_at')

        # Deleting field 'ProjectMember.updated_at'
        db.delete_column('projects_projectmember', 'updated_at')

        # Deleting field 'Project.created_at'
        db.delete_column('projects_project', 'created_at')

        # Deleting field 'Project.updated_at'
        db.delete_column('projects_project', 'updated_at')

        # Deleting field 'SprintTask.created_at'
        db.delete_column('projects_sprinttask', 'created_at')

        # Deleting field 'SprintTask.updated_at'
        db.delete_column('projects_sprinttask', 'updated_at')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'projects.productbacklog': {
            'Meta': {'object_name': 'ProductBacklog'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'project'", 'to': "orm['projects.Project']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'projects.productbacklogtask': {
            'Meta': {'object_name': 'ProductBacklogTask'},
            'backlog': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'backlog'", 'to': "orm['projects.ProductBacklog']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'demo_test': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'estimate': ('django.db.models.fields.FloatField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'max_length': '1000'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'projects.project': {
            'Meta': {'object_name': 'Project'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'projects.projectmember': {
            'Meta': {'object_name': 'ProjectMember'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'member'", 'to': "orm['projects.Project']"}),
            'role': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['projects.Role']", 'symmetrical': 'False'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'member_in_projects'", 'to': "orm['auth.User']"})
        },
        'projects.role': {
            'Meta': {'object_name': 'Role'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'projects.sprint': {
            'Meta': {'object_name': 'Sprint'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'deadline_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sprint_project'", 'to': "orm['projects.Project']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'projects.sprintbacklog': {
            'Meta': {'object_name': 'SprintBackLog'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sprint_backlogs'", 'to': "orm['projects.Project']"}),
            'sprint': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'backlog'", 'to': "orm['projects.Sprint']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'projects.sprinttask': {
            'Meta': {'object_name': 'SprintTask'},
            'assigner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tasks'", 'to': "orm['projects.ProjectMember']"}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'my_own_task'", 'to': "orm['projects.ProjectMember']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'deadline_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'progress': ('django.db.models.fields.FloatField', [], {'default': '0', 'max_length': '100', 'null': 'True'}),
            'sprint': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sprint_tasks'", 'to': "orm['projects.Sprint']"}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['projects.TaskStatus']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'tracker': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tracker_tasks'", 'to': "orm['projects.TaskTracker']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'projects.taskstatus': {
            'Meta': {'object_name': 'TaskStatus'},
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'projects.tasktracker': {
            'Meta': {'object_name': 'TaskTracker'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['projects']