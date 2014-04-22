# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.
        from project_share.models import Project as old_Project, FileUpload as old_FileUpload
        for project in old_Project.objects.all():
            p = old_FileUpload(f=project.project)
            p.save()
            s = old_FileUpload(f=project.screenshot)
            s.save()
            project.project2 = p
            project.screenshot2 = s
            project.save()

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'project_share.address': {
            'Meta': {'object_name': 'Address'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'teacher': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['project_share.ExtendedUser']", 'unique': 'True', 'primary_key': 'True'}),
            'town': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'project_share.application': {
            'Meta': {'object_name': 'Application'},
            'application_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'application_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project_share.ApplicationType']", 'null': 'True', 'blank': 'True'}),
            'class_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'codebase_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'more_info_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        u'project_share.applicationdemo': {
            'Meta': {'object_name': 'ApplicationDemo'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project_share.Application']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '1000', 'blank': 'True'}),
            'zipfile': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        u'project_share.applicationtype': {
            'Meta': {'object_name': 'ApplicationType'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'project_share.approval': {
            'Meta': {'object_name': 'Approval'},
            'approved_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project_share.ExtendedUser']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['project_share.Project']", 'unique': 'True'}),
            'when_requested': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'when_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'project_share.classroom': {
            'Meta': {'object_name': 'Classroom'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'students': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'student_classrooms'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['project_share.ExtendedUser']"}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'teacher_classrooms'", 'to': u"orm['project_share.ExtendedUser']"})
        },
        u'project_share.extendeduser': {
            'Meta': {'object_name': 'ExtendedUser'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'project_share.fileupload': {
            'Meta': {'object_name': 'FileUpload'},
            'f': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'project_share.project': {
            'Meta': {'unique_together': "(('name', 'owner'), ('project', 'owner'), ('screenshot', 'owner'))", 'object_name': 'Project'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project_share.Application']"}),
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project_share.ExtendedUser']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['project_share.FileUpload']"}),
            'screenshot': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['project_share.FileUpload']"})
        }
    }

    complete_apps = ['project_share']
    symmetrical = True
