# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'EspacioInnovacion.identificador'
        db.add_column(u'innovacion_espacioinnovacion', 'identificador',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'EspacioInnovacion.identificador'
        db.delete_column(u'innovacion_espacioinnovacion', 'identificador')


    models = {
        u'innovacion.actividadempresarial': {
            'Meta': {'object_name': 'ActividadEmpresarial'},
            'actividad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['innovacion.ActividadesEspacio']"}),
            'espacio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['innovacion.EspacioInnovacion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tema_1': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'act_temauno'", 'null': 'True', 'to': u"orm['innovacion.TemasIncidencia']"}),
            'tema_2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'act_temados'", 'null': 'True', 'to': u"orm['innovacion.TemasIncidencia']"}),
            'tema_3': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'act_tematres'", 'null': 'True', 'to': u"orm['innovacion.TemasIncidencia']"})
        },
        u'innovacion.actividadesespacio': {
            'Meta': {'object_name': 'ActividadesEspacio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'innovacion.actividadiniciativa': {
            'Meta': {'object_name': 'ActividadIniciativa'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'innovacion.espacioinnovacion': {
            'Meta': {'object_name': 'EspacioInnovacion'},
            'activos': ('django.db.models.fields.IntegerField', [], {}),
            'celular_contacto': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'cobertura': ('django.db.models.fields.IntegerField', [], {}),
            'correo_contacto': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'departamento_influye': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['lugar.Departamento']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identificador': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'municipios_influye': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['lugar.Municipio']", 'symmetrical': 'False'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nombre_contacto': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'numero_entidades': ('django.db.models.fields.IntegerField', [], {}),
            'papel': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['innovacion.PapelSimas']", 'symmetrical': 'False'}),
            'temas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['innovacion.TemasIncidencia']", 'symmetrical': 'False'}),
            'tiempo_formado': ('django.db.models.fields.IntegerField', [], {}),
            'tipos': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['innovacion.TipoEspacio']"}),
            'zona': ('django.db.models.fields.IntegerField', [], {})
        },
        u'innovacion.fotosiniciativa': {
            'Meta': {'object_name': 'FotosIniciativa'},
            'foto': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iniciativa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['innovacion.IniciativaInnovacion']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'innovacion.fotosinnovacion': {
            'Meta': {'object_name': 'FotosInnovacion'},
            'espacio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['innovacion.EspacioInnovacion']"}),
            'foto': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'innovacion.iniciativainnovacion': {
            'Meta': {'object_name': 'IniciativaInnovacion'},
            'acceso_mercado': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'actividades': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['innovacion.ActividadIniciativa']", 'null': 'True', 'blank': 'True'}),
            'analisis': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'comunicacion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'conservacion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'enfoque': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'espacio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['innovacion.EspacioInnovacion']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'fecha_finalizacion': ('django.db.models.fields.DateField', [], {}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {}),
            'fomento': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inversion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'problema': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'reduccion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'resultado': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sobre_tierra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'temas': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['innovacion.TemasAborda']", 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['innovacion.TipoIniciativa']"})
        },
        u'innovacion.papelsimas': {
            'Meta': {'object_name': 'PapelSimas'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'innovacion.temasaborda': {
            'Meta': {'object_name': 'TemasAborda'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'innovacion.temasincidencia': {
            'Meta': {'object_name': 'TemasIncidencia'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'innovacion.tipoespacio': {
            'Meta': {'object_name': 'TipoEspacio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'innovacion.tipoiniciativa': {
            'Meta': {'object_name': 'TipoIniciativa'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'lugar.departamento': {
            'Meta': {'object_name': 'Departamento'},
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Pais']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'})
        },
        u'lugar.municipio': {
            'Meta': {'ordering': "['departamento__nombre']", 'object_name': 'Municipio'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Departamento']"}),
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'})
        },
        u'lugar.pais': {
            'Meta': {'object_name': 'Pais'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['innovacion']