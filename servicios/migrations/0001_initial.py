# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OrganizacionSolicita'
        db.create_table(u'servicios_organizacionsolicita', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'servicios', ['OrganizacionSolicita'])

        # Adding model 'OrganizacionBenefician'
        db.create_table(u'servicios_organizacionbenefician', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'servicios', ['OrganizacionBenefician'])

        # Adding model 'TiposServicio'
        db.create_table(u'servicios_tiposservicio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'servicios', ['TiposServicio'])

        # Adding model 'TemasAbordan'
        db.create_table(u'servicios_temasabordan', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'servicios', ['TemasAbordan'])

        # Adding model 'TiposOrganizacionBenefician'
        db.create_table(u'servicios_tiposorganizacionbenefician', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'servicios', ['TiposOrganizacionBenefician'])

        # Adding model 'Servicios'
        db.create_table(u'servicios_servicios', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('solicita_servicio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['servicios.OrganizacionSolicita'])),
            ('monto', self.gf('django.db.models.fields.FloatField')()),
            ('fecha_inicio', self.gf('django.db.models.fields.DateField')()),
            ('fecha_finalizacion', self.gf('django.db.models.fields.DateField')()),
            ('objetivos', self.gf('django.db.models.fields.TextField')()),
            ('conclusiones', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'servicios', ['Servicios'])

        # Adding M2M table for field benefician_servicio on 'Servicios'
        db.create_table(u'servicios_servicios_benefician_servicio', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('servicios', models.ForeignKey(orm[u'servicios.servicios'], null=False)),
            ('organizacionbenefician', models.ForeignKey(orm[u'servicios.organizacionbenefician'], null=False))
        ))
        db.create_unique(u'servicios_servicios_benefician_servicio', ['servicios_id', 'organizacionbenefician_id'])

        # Adding M2M table for field tipos_servicios on 'Servicios'
        db.create_table(u'servicios_servicios_tipos_servicios', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('servicios', models.ForeignKey(orm[u'servicios.servicios'], null=False)),
            ('tiposservicio', models.ForeignKey(orm[u'servicios.tiposservicio'], null=False))
        ))
        db.create_unique(u'servicios_servicios_tipos_servicios', ['servicios_id', 'tiposservicio_id'])

        # Adding M2M table for field temas_abordan on 'Servicios'
        db.create_table(u'servicios_servicios_temas_abordan', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('servicios', models.ForeignKey(orm[u'servicios.servicios'], null=False)),
            ('temasabordan', models.ForeignKey(orm[u'servicios.temasabordan'], null=False))
        ))
        db.create_unique(u'servicios_servicios_temas_abordan', ['servicios_id', 'temasabordan_id'])

        # Adding M2M table for field org_benefician on 'Servicios'
        db.create_table(u'servicios_servicios_org_benefician', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('servicios', models.ForeignKey(orm[u'servicios.servicios'], null=False)),
            ('tiposorganizacionbenefician', models.ForeignKey(orm[u'servicios.tiposorganizacionbenefician'], null=False))
        ))
        db.create_unique(u'servicios_servicios_org_benefician', ['servicios_id', 'tiposorganizacionbenefician_id'])

        # Adding model 'EvaluacionServicio'
        db.create_table(u'servicios_evaluacionservicio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'servicios', ['EvaluacionServicio'])

        # Adding model 'ResultadoEvaluacion'
        db.create_table(u'servicios_resultadoevaluacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('servicio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['servicios.Servicios'])),
            ('evaluacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['servicios.EvaluacionServicio'])),
            ('escala', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'servicios', ['ResultadoEvaluacion'])

        # Adding model 'FotosServicios'
        db.create_table(u'servicios_fotosservicios', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('servicio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['servicios.Servicios'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('foto', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'servicios', ['FotosServicios'])


    def backwards(self, orm):
        # Deleting model 'OrganizacionSolicita'
        db.delete_table(u'servicios_organizacionsolicita')

        # Deleting model 'OrganizacionBenefician'
        db.delete_table(u'servicios_organizacionbenefician')

        # Deleting model 'TiposServicio'
        db.delete_table(u'servicios_tiposservicio')

        # Deleting model 'TemasAbordan'
        db.delete_table(u'servicios_temasabordan')

        # Deleting model 'TiposOrganizacionBenefician'
        db.delete_table(u'servicios_tiposorganizacionbenefician')

        # Deleting model 'Servicios'
        db.delete_table(u'servicios_servicios')

        # Removing M2M table for field benefician_servicio on 'Servicios'
        db.delete_table('servicios_servicios_benefician_servicio')

        # Removing M2M table for field tipos_servicios on 'Servicios'
        db.delete_table('servicios_servicios_tipos_servicios')

        # Removing M2M table for field temas_abordan on 'Servicios'
        db.delete_table('servicios_servicios_temas_abordan')

        # Removing M2M table for field org_benefician on 'Servicios'
        db.delete_table('servicios_servicios_org_benefician')

        # Deleting model 'EvaluacionServicio'
        db.delete_table(u'servicios_evaluacionservicio')

        # Deleting model 'ResultadoEvaluacion'
        db.delete_table(u'servicios_resultadoevaluacion')

        # Deleting model 'FotosServicios'
        db.delete_table(u'servicios_fotosservicios')


    models = {
        u'servicios.evaluacionservicio': {
            'Meta': {'object_name': 'EvaluacionServicio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'servicios.fotosservicios': {
            'Meta': {'object_name': 'FotosServicios'},
            'foto': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'servicio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['servicios.Servicios']"})
        },
        u'servicios.organizacionbenefician': {
            'Meta': {'object_name': 'OrganizacionBenefician'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'servicios.organizacionsolicita': {
            'Meta': {'object_name': 'OrganizacionSolicita'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'servicios.resultadoevaluacion': {
            'Meta': {'object_name': 'ResultadoEvaluacion'},
            'escala': ('django.db.models.fields.IntegerField', [], {}),
            'evaluacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['servicios.EvaluacionServicio']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'servicio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['servicios.Servicios']"})
        },
        u'servicios.servicios': {
            'Meta': {'object_name': 'Servicios'},
            'benefician_servicio': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['servicios.OrganizacionBenefician']", 'symmetrical': 'False'}),
            'conclusiones': ('django.db.models.fields.TextField', [], {}),
            'fecha_finalizacion': ('django.db.models.fields.DateField', [], {}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto': ('django.db.models.fields.FloatField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'objetivos': ('django.db.models.fields.TextField', [], {}),
            'org_benefician': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['servicios.TiposOrganizacionBenefician']", 'symmetrical': 'False'}),
            'solicita_servicio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['servicios.OrganizacionSolicita']"}),
            'temas_abordan': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['servicios.TemasAbordan']", 'symmetrical': 'False'}),
            'tipos_servicios': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['servicios.TiposServicio']", 'symmetrical': 'False'})
        },
        u'servicios.temasabordan': {
            'Meta': {'object_name': 'TemasAbordan'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'servicios.tiposorganizacionbenefician': {
            'Meta': {'object_name': 'TiposOrganizacionBenefician'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'servicios.tiposservicio': {
            'Meta': {'object_name': 'TiposServicio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['servicios']