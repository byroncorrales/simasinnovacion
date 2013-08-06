# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OrganizacionCampesina'
        db.create_table(u'promotores_organizacioncampesina', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'promotores', ['OrganizacionCampesina'])

        # Adding model 'OrganizacionCivil'
        db.create_table(u'promotores_organizacioncivil', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'promotores', ['OrganizacionCivil'])

        # Adding model 'EscuelaCampo'
        db.create_table(u'promotores_escuelacampo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'promotores', ['EscuelaCampo'])

        # Adding model 'CultivosFinca'
        db.create_table(u'promotores_cultivosfinca', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'promotores', ['CultivosFinca'])

        # Adding model 'AnimalesFinca'
        db.create_table(u'promotores_animalesfinca', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'promotores', ['AnimalesFinca'])

        # Adding model 'ProductoProcesado'
        db.create_table(u'promotores_productoprocesado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'promotores', ['ProductoProcesado'])

        # Adding model 'MercadoAcceso'
        db.create_table(u'promotores_mercadoacceso', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'promotores', ['MercadoAcceso'])

        # Adding model 'TipoSuelo'
        db.create_table(u'promotores_tiposuelo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'promotores', ['TipoSuelo'])

        # Adding model 'Promotor'
        db.create_table(u'promotores_promotor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('sexo', self.gf('django.db.models.fields.IntegerField')()),
            ('edad', self.gf('django.db.models.fields.IntegerField')()),
            ('educacion', self.gf('django.db.models.fields.IntegerField')()),
            ('contacto', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('activo', self.gf('django.db.models.fields.IntegerField')()),
            ('zona', self.gf('django.db.models.fields.IntegerField')()),
            ('departamento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lugar.Departamento'])),
            ('municipio', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['lugar.Municipio'])),
            ('gps', self.gf('geoposition.fields.GeopositionField')(max_length=42, null=True, blank=True)),
            ('organizacion_campesina', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['promotores.OrganizacionCampesina'])),
            ('organizacion_civil', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['promotores.OrganizacionCivil'])),
            ('escuela', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['promotores.EscuelaCampo'])),
            ('tipo_suelo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['promotores.TipoSuelo'])),
            ('tipo_clima', self.gf('django.db.models.fields.IntegerField')()),
            ('meses_lluvia', self.gf('django.db.models.fields.IntegerField')()),
            ('finca', self.gf('django.db.models.fields.FloatField')()),
            ('riego', self.gf('django.db.models.fields.IntegerField')()),
            ('bosque', self.gf('django.db.models.fields.FloatField')()),
            ('potrero', self.gf('django.db.models.fields.FloatField')()),
            ('tacotales', self.gf('django.db.models.fields.FloatField')()),
            ('forestal', self.gf('django.db.models.fields.FloatField')()),
            ('perennes', self.gf('django.db.models.fields.FloatField')()),
            ('lena', self.gf('django.db.models.fields.FloatField')()),
            ('anuales', self.gf('django.db.models.fields.FloatField')()),
            ('frutales', self.gf('django.db.models.fields.FloatField')()),
            ('potrero_abierto', self.gf('django.db.models.fields.FloatField')()),
            ('patio', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'promotores', ['Promotor'])

        # Adding M2M table for field cultivos_finca on 'Promotor'
        db.create_table(u'promotores_promotor_cultivos_finca', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('promotor', models.ForeignKey(orm[u'promotores.promotor'], null=False)),
            ('cultivosfinca', models.ForeignKey(orm[u'promotores.cultivosfinca'], null=False))
        ))
        db.create_unique(u'promotores_promotor_cultivos_finca', ['promotor_id', 'cultivosfinca_id'])

        # Adding M2M table for field animales_finca on 'Promotor'
        db.create_table(u'promotores_promotor_animales_finca', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('promotor', models.ForeignKey(orm[u'promotores.promotor'], null=False)),
            ('animalesfinca', models.ForeignKey(orm[u'promotores.animalesfinca'], null=False))
        ))
        db.create_unique(u'promotores_promotor_animales_finca', ['promotor_id', 'animalesfinca_id'])

        # Adding M2M table for field producto_procesado on 'Promotor'
        db.create_table(u'promotores_promotor_producto_procesado', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('promotor', models.ForeignKey(orm[u'promotores.promotor'], null=False)),
            ('productoprocesado', models.ForeignKey(orm[u'promotores.productoprocesado'], null=False))
        ))
        db.create_unique(u'promotores_promotor_producto_procesado', ['promotor_id', 'productoprocesado_id'])

        # Adding M2M table for field mercado_accede on 'Promotor'
        db.create_table(u'promotores_promotor_mercado_accede', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('promotor', models.ForeignKey(orm[u'promotores.promotor'], null=False)),
            ('mercadoacceso', models.ForeignKey(orm[u'promotores.mercadoacceso'], null=False))
        ))
        db.create_unique(u'promotores_promotor_mercado_accede', ['promotor_id', 'mercadoacceso_id'])

        # Adding model 'FotosPromotor'
        db.create_table(u'promotores_fotospromotor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('promotor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['promotores.Promotor'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('foto', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'promotores', ['FotosPromotor'])

        # Adding model 'TemasPruebas'
        db.create_table(u'promotores_temaspruebas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'promotores', ['TemasPruebas'])

        # Adding model 'RubroPruebas'
        db.create_table(u'promotores_rubropruebas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'promotores', ['RubroPruebas'])

        # Adding model 'EscalaPruebas'
        db.create_table(u'promotores_escalapruebas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'promotores', ['EscalaPruebas'])

        # Adding model 'PracticasProductivas'
        db.create_table(u'promotores_practicasproductivas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('promotor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['promotores.Promotor'])),
            ('nombre_prueba', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('fecha_prueba', self.gf('django.db.models.fields.DateField')()),
            ('tema_prueba', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['promotores.TemasPruebas'])),
            ('rubro_prueba', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['promotores.RubroPruebas'])),
            ('escala_prueba', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['promotores.EscalaPruebas'])),
            ('historia', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('fecha_inicio', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fecha_finalizacion', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('problema', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('agroecologico', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('aprobar', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('resultados', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('salud_planta', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('vida_suelo', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('prod_rendimiento', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('calidad_producto', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('plagas', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('costo', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'promotores', ['PracticasProductivas'])

        # Adding model 'DiasCampoPrueba'
        db.create_table(u'promotores_diascampoprueba', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('prueba', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['promotores.PracticasProductivas'])),
            ('fechas', self.gf('django.db.models.fields.DateField')()),
            ('hombres', self.gf('django.db.models.fields.IntegerField')()),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')()),
            ('comentario', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'promotores', ['DiasCampoPrueba'])

        # Adding model 'FotosPrueba'
        db.create_table(u'promotores_fotosprueba', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('practicas', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['promotores.PracticasProductivas'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('foto', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'promotores', ['FotosPrueba'])


    def backwards(self, orm):
        # Deleting model 'OrganizacionCampesina'
        db.delete_table(u'promotores_organizacioncampesina')

        # Deleting model 'OrganizacionCivil'
        db.delete_table(u'promotores_organizacioncivil')

        # Deleting model 'EscuelaCampo'
        db.delete_table(u'promotores_escuelacampo')

        # Deleting model 'CultivosFinca'
        db.delete_table(u'promotores_cultivosfinca')

        # Deleting model 'AnimalesFinca'
        db.delete_table(u'promotores_animalesfinca')

        # Deleting model 'ProductoProcesado'
        db.delete_table(u'promotores_productoprocesado')

        # Deleting model 'MercadoAcceso'
        db.delete_table(u'promotores_mercadoacceso')

        # Deleting model 'TipoSuelo'
        db.delete_table(u'promotores_tiposuelo')

        # Deleting model 'Promotor'
        db.delete_table(u'promotores_promotor')

        # Removing M2M table for field cultivos_finca on 'Promotor'
        db.delete_table('promotores_promotor_cultivos_finca')

        # Removing M2M table for field animales_finca on 'Promotor'
        db.delete_table('promotores_promotor_animales_finca')

        # Removing M2M table for field producto_procesado on 'Promotor'
        db.delete_table('promotores_promotor_producto_procesado')

        # Removing M2M table for field mercado_accede on 'Promotor'
        db.delete_table('promotores_promotor_mercado_accede')

        # Deleting model 'FotosPromotor'
        db.delete_table(u'promotores_fotospromotor')

        # Deleting model 'TemasPruebas'
        db.delete_table(u'promotores_temaspruebas')

        # Deleting model 'RubroPruebas'
        db.delete_table(u'promotores_rubropruebas')

        # Deleting model 'EscalaPruebas'
        db.delete_table(u'promotores_escalapruebas')

        # Deleting model 'PracticasProductivas'
        db.delete_table(u'promotores_practicasproductivas')

        # Deleting model 'DiasCampoPrueba'
        db.delete_table(u'promotores_diascampoprueba')

        # Deleting model 'FotosPrueba'
        db.delete_table(u'promotores_fotosprueba')


    models = {
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
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'promotores.cultivosfinca': {
            'Meta': {'object_name': 'CultivosFinca'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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