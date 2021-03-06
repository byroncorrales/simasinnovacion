# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CultivosFinca.image_cultivos'
        db.add_column(u'promotores_cultivosfinca', 'image_cultivos',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'AnimalesFinca.image_animales'
        db.add_column(u'promotores_animalesfinca', 'image_animales',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CultivosFinca.image_cultivos'
        db.delete_column(u'promotores_cultivosfinca', 'image_cultivos')

        # Deleting field 'AnimalesFinca.image_animales'
        db.delete_column(u'promotores_animalesfinca', 'image_animales')


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
        u'promotores.animalesfinca': {
            'Meta': {'object_name': 'AnimalesFinca'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_animales': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'promotores.cultivosfinca': {
            'Meta': {'object_name': 'CultivosFinca'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_cultivos': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'promotores.diascampoprueba': {
            'Meta': {'object_name': 'DiasCampoPrueba'},
            'comentario': ('django.db.models.fields.TextField', [], {}),
            'fechas': ('django.db.models.fields.DateField', [], {}),
            'hombres': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {}),
            'prueba': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['promotores.PracticasProductivas']"})
        },
        u'promotores.escalapruebas': {
            'Meta': {'object_name': 'EscalaPruebas'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'promotores.escuelacampo': {
            'Meta': {'object_name': 'EscuelaCampo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'promotores.fotospromotor': {
            'Meta': {'object_name': 'FotosPromotor'},
            'foto': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'promotor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['promotores.Promotor']"})
        },
        u'promotores.fotosprueba': {
            'Meta': {'object_name': 'FotosPrueba'},
            'foto': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'practicas': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['promotores.PracticasProductivas']"})
        },
        u'promotores.mercadoacceso': {
            'Meta': {'object_name': 'MercadoAcceso'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'promotores.organizacioncampesina': {
            'Meta': {'object_name': 'OrganizacionCampesina'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'promotores.organizacioncivil': {
            'Meta': {'object_name': 'OrganizacionCivil'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'promotores.practicasproductivas': {
            'Meta': {'object_name': 'PracticasProductivas'},
            'agroecologico': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'anio': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'aprobar': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'calidad_producto': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'costo': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'escala_prueba': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['promotores.EscalaPruebas']"}),
            'fecha_finalizacion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_prueba': ('django.db.models.fields.DateField', [], {}),
            'historia': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_prueba': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'plagas': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'problema': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'prod_rendimiento': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'promotor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['promotores.Promotor']"}),
            'resultados': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'rubro_prueba': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['promotores.RubroPruebas']"}),
            'salud_planta': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'tema_prueba': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['promotores.TemasPruebas']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'vida_suelo': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'promotores.productoprocesado': {
            'Meta': {'object_name': 'ProductoProcesado'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'promotores.promotor': {
            'Meta': {'object_name': 'Promotor'},
            'activo': ('django.db.models.fields.IntegerField', [], {}),
            'animales_finca': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['promotores.AnimalesFinca']", 'symmetrical': 'False'}),
            'anuales': ('django.db.models.fields.FloatField', [], {}),
            'bosque': ('django.db.models.fields.FloatField', [], {}),
            'contacto': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'cultivos_finca': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['promotores.CultivosFinca']", 'symmetrical': 'False'}),
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Departamento']"}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            'educacion': ('django.db.models.fields.IntegerField', [], {}),
            'escuela': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['promotores.EscuelaCampo']"}),
            'finca': ('django.db.models.fields.FloatField', [], {}),
            'forestal': ('django.db.models.fields.FloatField', [], {}),
            'frutales': ('django.db.models.fields.FloatField', [], {}),
            'gps': ('geoposition.fields.GeopositionField', [], {'max_length': '42', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identificador': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'lena': ('django.db.models.fields.FloatField', [], {}),
            'mercado_accede': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['promotores.MercadoAcceso']", 'symmetrical': 'False'}),
            'meses_lluvia': ('django.db.models.fields.IntegerField', [], {}),
            'municipio': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'organizacion_campesina': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['promotores.OrganizacionCampesina']"}),
            'organizacion_civil': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['promotores.OrganizacionCivil']"}),
            'patio': ('django.db.models.fields.FloatField', [], {}),
            'perennes': ('django.db.models.fields.FloatField', [], {}),
            'potrero': ('django.db.models.fields.FloatField', [], {}),
            'potrero_abierto': ('django.db.models.fields.FloatField', [], {}),
            'producto_procesado': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['promotores.ProductoProcesado']", 'symmetrical': 'False'}),
            'riego': ('django.db.models.fields.IntegerField', [], {}),
            'sexo': ('django.db.models.fields.IntegerField', [], {}),
            'tacotales': ('django.db.models.fields.FloatField', [], {}),
            'tipo_clima': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_suelo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['promotores.TipoSuelo']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'zona': ('django.db.models.fields.IntegerField', [], {})
        },
        u'promotores.rubropruebas': {
            'Meta': {'object_name': 'RubroPruebas'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'promotores.temaspruebas': {
            'Meta': {'object_name': 'TemasPruebas'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'promotores.tiposuelo': {
            'Meta': {'object_name': 'TipoSuelo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['promotores']