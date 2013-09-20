# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Empresas.usuario'
        db.add_column(u'empresas_empresas', 'usuario',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'MejoraEmpresas.usuario'
        db.add_column(u'empresas_mejoraempresas', 'usuario',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Empresas.usuario'
        db.delete_column(u'empresas_empresas', 'usuario_id')

        # Deleting field 'MejoraEmpresas.usuario'
        db.delete_column(u'empresas_mejoraempresas', 'usuario_id')


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
        u'empresas.actividadempresarial': {
            'Meta': {'object_name': 'ActividadEmpresarial'},
            'actividad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.ActividadesEmpresariales']"}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.Empresas']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rubro_1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rubro_2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rubro_3': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'empresas.actividadesempresariales': {
            'Meta': {'object_name': 'ActividadesEmpresariales'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'empresas.certificaciones': {
            'Meta': {'object_name': 'Certificaciones'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'empresas.certificacionesrubros': {
            'Meta': {'object_name': 'CertificacionesRubros'},
            'certificaciones': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.Certificaciones']"}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.Empresas']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rubro_1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rubro_2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rubro_3': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'empresas.compradoresrubros': {
            'Meta': {'object_name': 'CompradoresRubros'},
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.Empresas']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mercado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.MercadosCompradores']"}),
            'rubro_1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rubro_2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rubro_3': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'empresas.diascampoempresa': {
            'Meta': {'object_name': 'DiasCampoEmpresa'},
            'comentario': ('django.db.models.fields.TextField', [], {}),
            'fechas': ('django.db.models.fields.DateField', [], {}),
            'hombres': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mejora_empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.MejoraEmpresas']"}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {})
        },
        u'empresas.empresas': {
            'Meta': {'object_name': 'Empresas'},
            'activo': ('django.db.models.fields.IntegerField', [], {}),
            'contacto_celular': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'contacto_correo': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'contacto_nombre': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Departamento']"}),
            'formado_empresa': ('django.db.models.fields.IntegerField', [], {}),
            'gps': ('geoposition.fields.GeopositionField', [], {'max_length': '42', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identificador': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'municipio': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'organizacion_civil': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['promotores.OrganizacionCivil']"}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.TipoEmpresa']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'zona': ('django.db.models.fields.IntegerField', [], {})
        },
        u'empresas.fotosactividadempresarial': {
            'Meta': {'object_name': 'FotosActividadEmpresarial'},
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.Empresas']"}),
            'foto': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'empresas.fotosmejoraempresa': {
            'Meta': {'object_name': 'FotosMejoraEmpresa'},
            'foto': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mejora_empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.MejoraEmpresas']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'empresas.mejoraempresas': {
            'Meta': {'object_name': 'MejoraEmpresas'},
            'anio': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'causa': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.Empresas']"}),
            'fecha_finalizacion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_prueba': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inversion_credito': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'mejora_ingreso': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'mejora_precio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'mejora_proce_calidad': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'mejorar': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'mercado_prueba': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.Mercados']"}),
            'nombre_mejora': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'presentacion_acceso': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'problema': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'reduccion_costo': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'resultados': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'rubro_prueba': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.Rubros']"}),
            'tema_prueba': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.TemasEmpresa']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'volumen_acopio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'empresas.mercados': {
            'Meta': {'object_name': 'Mercados'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'empresas.mercadoscompradores': {
            'Meta': {'object_name': 'MercadosCompradores'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'empresas.mercadosrubros': {
            'Meta': {'object_name': 'MercadosRubros'},
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.Empresas']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mercado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.Mercados']"}),
            'rubro_1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rubro_2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rubro_3': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'empresas.rubros': {
            'Meta': {'object_name': 'Rubros'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'empresas.rubrosprincipales': {
            'Meta': {'object_name': 'RubrosPrincipales'},
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.Empresas']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto': ('django.db.models.fields.FloatField', [], {}),
            'prioridad': ('django.db.models.fields.IntegerField', [], {}),
            'rubro': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.Rubros']"}),
            'socias': ('django.db.models.fields.IntegerField', [], {}),
            'socios': ('django.db.models.fields.IntegerField', [], {}),
            'volumen': ('django.db.models.fields.FloatField', [], {})
        },
        u'empresas.temasempresa': {
            'Meta': {'object_name': 'TemasEmpresa'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'empresas.tipoempresa': {
            'Meta': {'object_name': 'TipoEmpresa'},
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
        },
        u'promotores.organizacioncivil': {
            'Meta': {'object_name': 'OrganizacionCivil'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['empresas']