# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TipoEspacio'
        db.create_table(u'politicas_tipoespacio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'politicas', ['TipoEspacio'])

        # Adding model 'PapelSimas'
        db.create_table(u'politicas_papelsimas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'politicas', ['PapelSimas'])

        # Adding model 'TemasIncidencia'
        db.create_table(u'politicas_temasincidencia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'politicas', ['TemasIncidencia'])

        # Adding model 'ActividadesEspacio'
        db.create_table(u'politicas_actividadesespacio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'politicas', ['ActividadesEspacio'])

        # Adding model 'EspacioInnovacion'
        db.create_table(u'politicas_espacioinnovacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('tipos', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['politicas.TipoEspacio'])),
            ('activos', self.gf('django.db.models.fields.IntegerField')()),
            ('tiempo_formado', self.gf('django.db.models.fields.IntegerField')()),
            ('nombre_contacto', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('celular_contacto', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('correo_contacto', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('zona', self.gf('django.db.models.fields.IntegerField')()),
            ('cobertura', self.gf('django.db.models.fields.IntegerField')()),
            ('numero_entidades', self.gf('django.db.models.fields.IntegerField')()),
            ('identificador', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'politicas', ['EspacioInnovacion'])

        # Adding M2M table for field departamento_influye on 'EspacioInnovacion'
        db.create_table(u'politicas_espacioinnovacion_departamento_influye', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('espacioinnovacion', models.ForeignKey(orm[u'politicas.espacioinnovacion'], null=False)),
            ('departamento', models.ForeignKey(orm[u'lugar.departamento'], null=False))
        ))
        db.create_unique(u'politicas_espacioinnovacion_departamento_influye', ['espacioinnovacion_id', 'departamento_id'])

        # Adding M2M table for field municipios_influye on 'EspacioInnovacion'
        db.create_table(u'politicas_espacioinnovacion_municipios_influye', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('espacioinnovacion', models.ForeignKey(orm[u'politicas.espacioinnovacion'], null=False)),
            ('municipio', models.ForeignKey(orm[u'lugar.municipio'], null=False))
        ))
        db.create_unique(u'politicas_espacioinnovacion_municipios_influye', ['espacioinnovacion_id', 'municipio_id'])

        # Adding M2M table for field papel on 'EspacioInnovacion'
        db.create_table(u'politicas_espacioinnovacion_papel', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('espacioinnovacion', models.ForeignKey(orm[u'politicas.espacioinnovacion'], null=False)),
            ('papelsimas', models.ForeignKey(orm[u'politicas.papelsimas'], null=False))
        ))
        db.create_unique(u'politicas_espacioinnovacion_papel', ['espacioinnovacion_id', 'papelsimas_id'])

        # Adding M2M table for field temas on 'EspacioInnovacion'
        db.create_table(u'politicas_espacioinnovacion_temas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('espacioinnovacion', models.ForeignKey(orm[u'politicas.espacioinnovacion'], null=False)),
            ('temasincidencia', models.ForeignKey(orm[u'politicas.temasincidencia'], null=False))
        ))
        db.create_unique(u'politicas_espacioinnovacion_temas', ['espacioinnovacion_id', 'temasincidencia_id'])

        # Adding model 'ActividadEmpresarial'
        db.create_table(u'politicas_actividadempresarial', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('espacio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['politicas.EspacioInnovacion'])),
            ('actividad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['politicas.ActividadesEspacio'])),
            ('tema_1', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('tema_2', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('tema_3', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'politicas', ['ActividadEmpresarial'])

        # Adding model 'FotosInnovacion'
        db.create_table(u'politicas_fotosinnovacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('espacio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['politicas.EspacioInnovacion'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('foto', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'politicas', ['FotosInnovacion'])

        # Adding model 'TipoIniciativa'
        db.create_table(u'politicas_tipoiniciativa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'politicas', ['TipoIniciativa'])

        # Adding model 'TemasAborda'
        db.create_table(u'politicas_temasaborda', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'politicas', ['TemasAborda'])

        # Adding model 'ActividadIniciativa'
        db.create_table(u'politicas_actividadiniciativa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'politicas', ['ActividadIniciativa'])

        # Adding model 'IniciativaInnovacion'
        db.create_table(u'politicas_iniciativainnovacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('espacio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['politicas.EspacioInnovacion'])),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['politicas.TipoIniciativa'])),
            ('fecha_inicio', self.gf('django.db.models.fields.DateField')()),
            ('fecha_finalizacion', self.gf('django.db.models.fields.DateField')()),
            ('problema', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('analisis', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('enfoque', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('resultado', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('sobre_tierra', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('fomento', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('conservacion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('inversion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('acceso_mercado', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('comunicacion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('reduccion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'politicas', ['IniciativaInnovacion'])

        # Adding M2M table for field temas on 'IniciativaInnovacion'
        db.create_table(u'politicas_iniciativainnovacion_temas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('iniciativainnovacion', models.ForeignKey(orm[u'politicas.iniciativainnovacion'], null=False)),
            ('temasaborda', models.ForeignKey(orm[u'politicas.temasaborda'], null=False))
        ))
        db.create_unique(u'politicas_iniciativainnovacion_temas', ['iniciativainnovacion_id', 'temasaborda_id'])

        # Adding M2M table for field actividades on 'IniciativaInnovacion'
        db.create_table(u'politicas_iniciativainnovacion_actividades', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('iniciativainnovacion', models.ForeignKey(orm[u'politicas.iniciativainnovacion'], null=False)),
            ('actividadiniciativa', models.ForeignKey(orm[u'politicas.actividadiniciativa'], null=False))
        ))
        db.create_unique(u'politicas_iniciativainnovacion_actividades', ['iniciativainnovacion_id', 'actividadiniciativa_id'])

        # Adding model 'FotosIniciativa'
        db.create_table(u'politicas_fotosiniciativa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('iniciativa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['politicas.IniciativaInnovacion'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('foto', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'politicas', ['FotosIniciativa'])


    def backwards(self, orm):
        # Deleting model 'TipoEspacio'
        db.delete_table(u'politicas_tipoespacio')

        # Deleting model 'PapelSimas'
        db.delete_table(u'politicas_papelsimas')

        # Deleting model 'TemasIncidencia'
        db.delete_table(u'politicas_temasincidencia')

        # Deleting model 'ActividadesEspacio'
        db.delete_table(u'politicas_actividadesespacio')

        # Deleting model 'EspacioInnovacion'
        db.delete_table(u'politicas_espacioinnovacion')

        # Removing M2M table for field departamento_influye on 'EspacioInnovacion'
        db.delete_table('politicas_espacioinnovacion_departamento_influye')

        # Removing M2M table for field municipios_influye on 'EspacioInnovacion'
        db.delete_table('politicas_espacioinnovacion_municipios_influye')

        # Removing M2M table for field papel on 'EspacioInnovacion'
        db.delete_table('politicas_espacioinnovacion_papel')

        # Removing M2M table for field temas on 'EspacioInnovacion'
        db.delete_table('politicas_espacioinnovacion_temas')

        # Deleting model 'ActividadEmpresarial'
        db.delete_table(u'politicas_actividadempresarial')

        # Deleting model 'FotosInnovacion'
        db.delete_table(u'politicas_fotosinnovacion')

        # Deleting model 'TipoIniciativa'
        db.delete_table(u'politicas_tipoiniciativa')

        # Deleting model 'TemasAborda'
        db.delete_table(u'politicas_temasaborda')

        # Deleting model 'ActividadIniciativa'
        db.delete_table(u'politicas_actividadiniciativa')

        # Deleting model 'IniciativaInnovacion'
        db.delete_table(u'politicas_iniciativainnovacion')

        # Removing M2M table for field temas on 'IniciativaInnovacion'
        db.delete_table('politicas_iniciativainnovacion_temas')

        # Removing M2M table for field actividades on 'IniciativaInnovacion'
        db.delete_table('politicas_iniciativainnovacion_actividades')

        # Deleting model 'FotosIniciativa'
        db.delete_table(u'politicas_fotosiniciativa')


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
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['politicas.TipoIniciativa']"})
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