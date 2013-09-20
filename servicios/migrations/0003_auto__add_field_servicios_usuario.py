# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Servicios.usuario'
        db.add_column(u'servicios_servicios', 'usuario',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Servicios.usuario'
        db.delete_column(u'servicios_servicios', 'usuario_id')


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
            'tipos_servicios': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['servicios.TiposServicio']", 'symmetrical': 'False'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
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