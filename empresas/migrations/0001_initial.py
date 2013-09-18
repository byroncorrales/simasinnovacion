# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TipoEmpresa'
        db.create_table(u'empresas_tipoempresa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'empresas', ['TipoEmpresa'])

        # Adding model 'Rubros'
        db.create_table(u'empresas_rubros', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'empresas', ['Rubros'])

        # Adding model 'Empresas'
        db.create_table(u'empresas_empresas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.TipoEmpresa'])),
            ('activo', self.gf('django.db.models.fields.IntegerField')()),
            ('formado_empresa', self.gf('django.db.models.fields.IntegerField')()),
            ('contacto_nombre', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('contacto_celular', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('contacto_correo', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('zona', self.gf('django.db.models.fields.IntegerField')()),
            ('departamento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lugar.Departamento'])),
            ('municipio', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['lugar.Municipio'])),
            ('gps', self.gf('geoposition.fields.GeopositionField')(max_length=42, null=True, blank=True)),
            ('organizacion_civil', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['promotores.OrganizacionCivil'])),
            ('identificador', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'empresas', ['Empresas'])

        # Adding model 'RubrosPrincipales'
        db.create_table(u'empresas_rubrosprincipales', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.Empresas'])),
            ('prioridad', self.gf('django.db.models.fields.IntegerField')()),
            ('rubro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.Rubros'])),
            ('volumen', self.gf('django.db.models.fields.FloatField')()),
            ('monto', self.gf('django.db.models.fields.FloatField')()),
            ('socios', self.gf('django.db.models.fields.IntegerField')()),
            ('socias', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'empresas', ['RubrosPrincipales'])

        # Adding model 'ActividadesEmpresariales'
        db.create_table(u'empresas_actividadesempresariales', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'empresas', ['ActividadesEmpresariales'])

        # Adding model 'Mercados'
        db.create_table(u'empresas_mercados', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'empresas', ['Mercados'])

        # Adding model 'MercadosCompradores'
        db.create_table(u'empresas_mercadoscompradores', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'empresas', ['MercadosCompradores'])

        # Adding model 'Certificaciones'
        db.create_table(u'empresas_certificaciones', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'empresas', ['Certificaciones'])

        # Adding model 'ActividadEmpresarial'
        db.create_table(u'empresas_actividadempresarial', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.Empresas'])),
            ('actividad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.ActividadesEmpresariales'])),
            ('rubro_1', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('rubro_2', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('rubro_3', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'empresas', ['ActividadEmpresarial'])

        # Adding model 'MercadosRubros'
        db.create_table(u'empresas_mercadosrubros', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.Empresas'])),
            ('mercado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.Mercados'])),
            ('rubro_1', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('rubro_2', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('rubro_3', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'empresas', ['MercadosRubros'])

        # Adding model 'CompradoresRubros'
        db.create_table(u'empresas_compradoresrubros', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.Empresas'])),
            ('mercado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.MercadosCompradores'])),
            ('rubro_1', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('rubro_2', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('rubro_3', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'empresas', ['CompradoresRubros'])

        # Adding model 'CertificacionesRubros'
        db.create_table(u'empresas_certificacionesrubros', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.Empresas'])),
            ('certificaciones', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.Certificaciones'])),
            ('rubro_1', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('rubro_2', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('rubro_3', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'empresas', ['CertificacionesRubros'])

        # Adding model 'FotosActividadEmpresarial'
        db.create_table(u'empresas_fotosactividadempresarial', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.Empresas'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('foto', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'empresas', ['FotosActividadEmpresarial'])

        # Adding model 'TemasEmpresa'
        db.create_table(u'empresas_temasempresa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'empresas', ['TemasEmpresa'])

        # Adding model 'MejoraEmpresas'
        db.create_table(u'empresas_mejoraempresas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_mejora', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.Empresas'])),
            ('fecha_prueba', self.gf('django.db.models.fields.DateField')()),
            ('tema_prueba', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.TemasEmpresa'])),
            ('rubro_prueba', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.Rubros'])),
            ('mercado_prueba', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.Mercados'])),
            ('fecha_inicio', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fecha_finalizacion', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('problema', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('causa', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('mejorar', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('resultados', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('volumen_acopio', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('mejora_proce_calidad', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('presentacion_acceso', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('inversion_credito', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('mejora_precio', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('mejora_ingreso', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('reduccion_costo', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('anio', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'empresas', ['MejoraEmpresas'])

        # Adding model 'DiasCampoEmpresa'
        db.create_table(u'empresas_diascampoempresa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mejora_empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.MejoraEmpresas'])),
            ('fechas', self.gf('django.db.models.fields.DateField')()),
            ('hombres', self.gf('django.db.models.fields.IntegerField')()),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')()),
            ('comentario', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'empresas', ['DiasCampoEmpresa'])

        # Adding model 'FotosMejoraEmpresa'
        db.create_table(u'empresas_fotosmejoraempresa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mejora_empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.MejoraEmpresas'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('foto', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'empresas', ['FotosMejoraEmpresa'])


    def backwards(self, orm):
        # Deleting model 'TipoEmpresa'
        db.delete_table(u'empresas_tipoempresa')

        # Deleting model 'Rubros'
        db.delete_table(u'empresas_rubros')

        # Deleting model 'Empresas'
        db.delete_table(u'empresas_empresas')

        # Deleting model 'RubrosPrincipales'
        db.delete_table(u'empresas_rubrosprincipales')

        # Deleting model 'ActividadesEmpresariales'
        db.delete_table(u'empresas_actividadesempresariales')

        # Deleting model 'Mercados'
        db.delete_table(u'empresas_mercados')

        # Deleting model 'MercadosCompradores'
        db.delete_table(u'empresas_mercadoscompradores')

        # Deleting model 'Certificaciones'
        db.delete_table(u'empresas_certificaciones')

        # Deleting model 'ActividadEmpresarial'
        db.delete_table(u'empresas_actividadempresarial')

        # Deleting model 'MercadosRubros'
        db.delete_table(u'empresas_mercadosrubros')

        # Deleting model 'CompradoresRubros'
        db.delete_table(u'empresas_compradoresrubros')

        # Deleting model 'CertificacionesRubros'
        db.delete_table(u'empresas_certificacionesrubros')

        # Deleting model 'FotosActividadEmpresarial'
        db.delete_table(u'empresas_fotosactividadempresarial')

        # Deleting model 'TemasEmpresa'
        db.delete_table(u'empresas_temasempresa')

        # Deleting model 'MejoraEmpresas'
        db.delete_table(u'empresas_mejoraempresas')

        # Deleting model 'DiasCampoEmpresa'
        db.delete_table(u'empresas_diascampoempresa')

        # Deleting model 'FotosMejoraEmpresa'
        db.delete_table(u'empresas_fotosmejoraempresa')


    models = {
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