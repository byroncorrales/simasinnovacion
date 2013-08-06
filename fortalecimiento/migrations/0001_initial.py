# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TiposMedios'
        db.create_table(u'fortalecimiento_tiposmedios', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'fortalecimiento', ['TiposMedios'])

        # Adding model 'TemasAbordan'
        db.create_table(u'fortalecimiento_temasabordan', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'fortalecimiento', ['TemasAbordan'])

        # Adding model 'GruposMetas'
        db.create_table(u'fortalecimiento_gruposmetas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'fortalecimiento', ['GruposMetas'])

        # Adding model 'PapelSimas'
        db.create_table(u'fortalecimiento_papelsimas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'fortalecimiento', ['PapelSimas'])

        # Adding model 'MediosFortalecimiento'
        db.create_table(u'fortalecimiento_mediosfortalecimiento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('fecha_inicio', self.gf('django.db.models.fields.DateField')()),
            ('fecha_finalizacion', self.gf('django.db.models.fields.DateField')()),
            ('objetivos', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'fortalecimiento', ['MediosFortalecimiento'])

        # Adding M2M table for field tipo_medio on 'MediosFortalecimiento'
        db.create_table(u'fortalecimiento_mediosfortalecimiento_tipo_medio', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mediosfortalecimiento', models.ForeignKey(orm[u'fortalecimiento.mediosfortalecimiento'], null=False)),
            ('tiposmedios', models.ForeignKey(orm[u'fortalecimiento.tiposmedios'], null=False))
        ))
        db.create_unique(u'fortalecimiento_mediosfortalecimiento_tipo_medio', ['mediosfortalecimiento_id', 'tiposmedios_id'])

        # Adding M2M table for field temas on 'MediosFortalecimiento'
        db.create_table(u'fortalecimiento_mediosfortalecimiento_temas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mediosfortalecimiento', models.ForeignKey(orm[u'fortalecimiento.mediosfortalecimiento'], null=False)),
            ('temasabordan', models.ForeignKey(orm[u'fortalecimiento.temasabordan'], null=False))
        ))
        db.create_unique(u'fortalecimiento_mediosfortalecimiento_temas', ['mediosfortalecimiento_id', 'temasabordan_id'])

        # Adding M2M table for field grupos_metas on 'MediosFortalecimiento'
        db.create_table(u'fortalecimiento_mediosfortalecimiento_grupos_metas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mediosfortalecimiento', models.ForeignKey(orm[u'fortalecimiento.mediosfortalecimiento'], null=False)),
            ('gruposmetas', models.ForeignKey(orm[u'fortalecimiento.gruposmetas'], null=False))
        ))
        db.create_unique(u'fortalecimiento_mediosfortalecimiento_grupos_metas', ['mediosfortalecimiento_id', 'gruposmetas_id'])

        # Adding M2M table for field papel_simas on 'MediosFortalecimiento'
        db.create_table(u'fortalecimiento_mediosfortalecimiento_papel_simas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mediosfortalecimiento', models.ForeignKey(orm[u'fortalecimiento.mediosfortalecimiento'], null=False)),
            ('papelsimas', models.ForeignKey(orm[u'fortalecimiento.papelsimas'], null=False))
        ))
        db.create_unique(u'fortalecimiento_mediosfortalecimiento_papel_simas', ['mediosfortalecimiento_id', 'papelsimas_id'])

        # Adding model 'PersonasResultados'
        db.create_table(u'fortalecimiento_personasresultados', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'fortalecimiento', ['PersonasResultados'])

        # Adding model 'Participantes'
        db.create_table(u'fortalecimiento_participantes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('medios', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fortalecimiento.MediosFortalecimiento'])),
            ('opcion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fortalecimiento.PersonasResultados'])),
            ('hombres', self.gf('django.db.models.fields.IntegerField')()),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'fortalecimiento', ['Participantes'])

        # Adding model 'NivelConocimiento'
        db.create_table(u'fortalecimiento_nivelconocimiento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('medios', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fortalecimiento.MediosFortalecimiento'])),
            ('opcion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fortalecimiento.PersonasResultados'])),
            ('ante_evento', self.gf('django.db.models.fields.IntegerField')()),
            ('despues_evento', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'fortalecimiento', ['NivelConocimiento'])

        # Adding model 'FotosMedios'
        db.create_table(u'fortalecimiento_fotosmedios', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('medios', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fortalecimiento.MediosFortalecimiento'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('foto', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'fortalecimiento', ['FotosMedios'])


    def backwards(self, orm):
        # Deleting model 'TiposMedios'
        db.delete_table(u'fortalecimiento_tiposmedios')

        # Deleting model 'TemasAbordan'
        db.delete_table(u'fortalecimiento_temasabordan')

        # Deleting model 'GruposMetas'
        db.delete_table(u'fortalecimiento_gruposmetas')

        # Deleting model 'PapelSimas'
        db.delete_table(u'fortalecimiento_papelsimas')

        # Deleting model 'MediosFortalecimiento'
        db.delete_table(u'fortalecimiento_mediosfortalecimiento')

        # Removing M2M table for field tipo_medio on 'MediosFortalecimiento'
        db.delete_table('fortalecimiento_mediosfortalecimiento_tipo_medio')

        # Removing M2M table for field temas on 'MediosFortalecimiento'
        db.delete_table('fortalecimiento_mediosfortalecimiento_temas')

        # Removing M2M table for field grupos_metas on 'MediosFortalecimiento'
        db.delete_table('fortalecimiento_mediosfortalecimiento_grupos_metas')

        # Removing M2M table for field papel_simas on 'MediosFortalecimiento'
        db.delete_table('fortalecimiento_mediosfortalecimiento_papel_simas')

        # Deleting model 'PersonasResultados'
        db.delete_table(u'fortalecimiento_personasresultados')

        # Deleting model 'Participantes'
        db.delete_table(u'fortalecimiento_participantes')

        # Deleting model 'NivelConocimiento'
        db.delete_table(u'fortalecimiento_nivelconocimiento')

        # Deleting model 'FotosMedios'
        db.delete_table(u'fortalecimiento_fotosmedios')


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