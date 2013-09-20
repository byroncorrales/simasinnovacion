# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'IniciativaInnovacion.usuario'
        db.add_column(u'politicas_iniciativainnovacion', 'usuario',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'EspacioInnovacion.usuario'
        db.add_column(u'politicas_espacioinnovacion', 'usuario',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'IniciativaInnovacion.usuario'
        db.delete_column(u'politicas_iniciativainnovacion', 'usuario_id')

        # Deleting field 'EspacioInnovacion.usuario'
        db.delete_column(u'politicas_espacioinnovacion', 'usuario_id')


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
        },
        u'politicas.actividadempresarial': {
            'Meta': {'object_name': 'ActividadEmpresarial'},
            'actividad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['politicas.ActividadesEspacio']"}),
            'espacio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['politicas.EspacioInnovacion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tema_1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tema_2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tema_3': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'politicas.actividadesespacio': {
            'Meta': {'object_name': 'ActividadesEspacio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'politicas.actividadiniciativa': {
            'Meta': {'object_name': 'ActividadIniciativa'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'politicas.espacioinnovacion': {
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
            'papel': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['politicas.PapelSimas']", 'symmetrical': 'False'}),
            'temas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['politicas.TemasIncidencia']", 'symmetrical': 'False'}),
            'tiempo_formado': ('django.db.models.fields.IntegerField', [], {}),
            'tipos': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['politicas.TipoEspacio']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'zona': ('django.db.models.fields.IntegerField', [], {})
        },
        u'politicas.fotosiniciativa': {
            'Meta': {'object_name': 'FotosIniciativa'},
            'foto': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iniciativa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['politicas.IniciativaInnovacion']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'politicas.fotosinnovacion': {
            'Meta': {'object_name': 'FotosInnovacion'},
            'espacio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['politicas.EspacioInnovacion']"}),
            'foto': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'politicas.iniciativainnovacion': {
            'Meta': {'object_name': 'IniciativaInnovacion'},
            'acceso_mercado': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'actividades': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['politicas.ActividadIniciativa']", 'null': 'True', 'blank': 'True'}),
            'analisis': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'comunicacion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'conservacion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'enfoque': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'espacio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['politicas.EspacioInnovacion']"}),
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
            'temas': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['politicas.TemasAborda']", 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['politicas.TipoIniciativa']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'politicas.papelsimas': {
            'Meta': {'object_name': 'PapelSimas'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'politicas.temasaborda': {
            'Meta': {'object_name': 'TemasAborda'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'politicas.temasincidencia': {
            'Meta': {'object_name': 'TemasIncidencia'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'politicas.tipoespacio': {
            'Meta': {'object_name': 'TipoEspacio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'politicas.tipoiniciativa': {
            'Meta': {'object_name': 'TipoIniciativa'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['politicas']