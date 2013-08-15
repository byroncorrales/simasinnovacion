# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MediosFortalecimiento.fecha'
        db.add_column(u'fortalecimiento_mediosfortalecimiento', 'fecha',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MediosFortalecimiento.fecha'
        db.delete_column(u'fortalecimiento_mediosfortalecimiento', 'fecha')


    models = {
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
            'tipo_medio': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['fortalecimiento.TiposMedios']", 'symmetrical': 'False'})
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