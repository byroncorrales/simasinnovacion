# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Servicios.fecha'
        db.add_column(u'servicios_servicios', 'fecha',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Servicios.fecha'
        db.delete_column(u'servicios_servicios', 'fecha')


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
            'fecha': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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