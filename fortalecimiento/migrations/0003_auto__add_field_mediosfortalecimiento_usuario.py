# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MediosFortalecimiento.usuario'
        db.add_column(u'fortalecimiento_mediosfortalecimiento', 'usuario',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MediosFortalecimiento.usuario'
        db.delete_column(u'fortalecimiento_mediosfortalecimiento', 'usuario_id')


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
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'fortalecimiento.fotosmedios': {
            'Meta': {'object_name': 'FotosMedios'},
            'foto': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medios': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fortalecimiento.MediosFortalecimiento']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'fortalecimiento.gruposmetas': {
            'Meta': {'object_name': 'GruposMetas'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'fortalecimiento.mediosfortalecimiento': {
            'Meta': {'object_name': 'MediosFortalecimiento'},
            'fecha': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_finalizacion': ('django.db.models.fields.DateField', [], {}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {}),
            'grupos_metas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['fortalecimiento.GruposMetas']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'objetivos': ('django.db.models.fields.TextField', [], {}),
            'papel_simas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['fortalecimiento.PapelSimas']", 'symmetrical': 'False'}),
            'temas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['fortalecimiento.TemasAbordan']", 'symmetrical': 'False'}),
            'tipo_medio': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['fortalecimiento.TiposMedios']", 'symmetrical': 'False'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'fortalecimiento.nivelconocimiento': {
            'Meta': {'object_name': 'NivelConocimiento'},
            'ante_evento': ('django.db.models.fields.IntegerField', [], {}),
            'despues_evento': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medios': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fortalecimiento.MediosFortalecimiento']"}),
            'opcion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fortalecimiento.PersonasResultados']"})
        },
        u'fortalecimiento.papelsimas': {
            'Meta': {'object_name': 'PapelSimas'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'fortalecimiento.participantes': {
            'Meta': {'object_name': 'Participantes'},
            'hombres': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medios': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fortalecimiento.MediosFortalecimiento']"}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {}),
            'opcion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fortalecimiento.PersonasResultados']"})
        },
        u'fortalecimiento.personasresultados': {
            'Meta': {'object_name': 'PersonasResultados'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'fortalecimiento.temasabordan': {
            'Meta': {'object_name': 'TemasAbordan'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'fortalecimiento.tiposmedios': {
            'Meta': {'object_name': 'TiposMedios'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['fortalecimiento']