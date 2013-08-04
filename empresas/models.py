#encoding: utf-8

from django.db import models
from lugar.models import Departamento, Municipio
from smart_selects.db_fields import ChainedForeignKey
from geoposition.fields import GeopositionField
from sorl.thumbnail import ImageField
from simasinnovacion.utils import get_file_path 
from promotores.models import OrganizacionCivil

#modelos utiles para la fichas de empresas y practicas empresariales
class TipoEmpresa(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipos de empresas"

class Rubros(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Rubros"

#-----------------------------------------------------------
#                  ficha de las empresas rurales
#-----------------------------------------------------------
class Empresas(models.Model):
    nombre = models.CharField('Nombre empresa', max_length=200)
    tipo = models.ForeignKey(TipoEmpresa, verbose_name='Tipo de empresa')
    activo = models.IntegerField(choices=((1,'2013'),(2,'2014'),
                                (3,'2015'),(4,'2016'),),
                    verbose_name='Años activo en prueba de prácticas empresariales')
    formado_empresa = models.IntegerField('Años de haber formado la empresa')
    contacto_nombre = models.CharField(max_length=200, null=True, blank=True)
    contacto_celular = models.CharField(max_length=50, null=True, blank=True)
    contacto_correo = models.EmailField(null=True, blank=True)
    zona = models.IntegerField(choices=((1, 'Seca'),(2, 'Alta'),(3, 'Húmeda'),))
    departamento = models.ForeignKey(Departamento)
    municipio = ChainedForeignKey(
        Municipio,
        chained_field="departamento",
        chained_model_field="departamento",
        show_all=False,
        auto_choose=True
    )
    gps = GeopositionField(null=True, blank=True)
    organizacion_civil = models.ForeignKey(OrganizacionCivil,
                         verbose_name=u'Nombre Organización de sociedad civil que apoya')

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Empresa rural'
        verbose_name_plural = "Empresas rurales"

#------------------- fin -----------------------------

class RubrosPrincipales(models.Model):
    empresa = models.ForeignKey(Empresas)
    prioridad = models.IntegerField(choices=((1, '1'),(2, '2'),(3, '3'),))
    rubro = models.ForeignKey(Rubros)
    volumen = models.FloatField('Volumen de venta (unidad)')
    monto = models.FloatField('Monto de venta C$')
    socios = models.IntegerField()
    socias = models.IntegerField()

    def __unicode__(self):
        return u'%s' % str(self.prioridad)

    class Meta:
        verbose_name_plural = "Rubros principales de la empresa" 

class ActividadesEmpresariales(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Actividades Empresariales"

class Mercados(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Mercados"

class Certificaciones(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Certificaciones"

class ActividadEmpresarial(models.Model):
    empresa = models.ForeignKey(Empresas)
    actividad = models.ForeignKey(ActividadesEmpresariales)
    rubro_1 = models.ForeignKey(Rubros, related_name="act_rubrouno", null=True, blank=True)
    rubro_2 = models.ForeignKey(Rubros, related_name="act_rubrodos", null=True, blank=True)
    rubro_3 = models.ForeignKey(Rubros, related_name="act_rubrotres", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Actividad empresarial relacionadas a los rubros"

class MercadosRubros(models.Model):
    empresa = models.ForeignKey(Empresas)
    mercado = models.ForeignKey(Mercados)
    rubro_1 = models.ForeignKey(Rubros, related_name="mer_rubrouno", null=True, blank=True)
    rubro_2 = models.ForeignKey(Rubros, related_name="mer_rubrodos", null=True, blank=True)
    rubro_3 = models.ForeignKey(Rubros, related_name="mer_rubrotres", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Mercados de los rubros"

class CompradoresRubros(models.Model):
    empresa = models.ForeignKey(Empresas)
    mercado = models.ForeignKey(Mercados)
    rubro_1 = models.ForeignKey(Rubros, related_name="com_rubrouno", null=True, blank=True)
    rubro_2 = models.ForeignKey(Rubros, related_name="com_rubrodos", null=True, blank=True)
    rubro_3 = models.ForeignKey(Rubros, related_name="com_rubrotres", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Compradores de los rubros"

class CertificacionesRubros(models.Model):
    empresa = models.ForeignKey(Empresas)
    certificaciones = models.ForeignKey(Certificaciones)
    rubro_1 = models.ForeignKey(Rubros, related_name="cer_rubrouno", null=True, blank=True)
    rubro_2 = models.ForeignKey(Rubros, related_name="cer_rubrodos", null=True, blank=True)
    rubro_3 = models.ForeignKey(Rubros, related_name="cer_rubrotres", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Certificaciones de los rubros"

class FotosActividadEmpresarial(models.Model):
    empresa = models.ForeignKey(Empresas)
    nombre = models.CharField(max_length=200)
    foto = ImageField(upload_to=get_file_path, blank=True, null=True)

    fileDir = 'fotoEmpresarural/'

    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Fotos de las actividades de la empresa rural"

#---------------------------------------------------------------------
#               ficha sobre practicas empresariales
#---------------------------------------------------------------------

