#encoding: utf-8

from django.db import models
from lugar.models import Departamento, Municipio
from smart_selects.db_fields import ChainedForeignKey
from geoposition.fields import GeopositionField
from sorl.thumbnail import ImageField
from simasinnovacion.utils import get_file_path 
from promotores.models import OrganizacionCivil
from django.contrib.auth.models import User

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

    identificador = models.IntegerField(editable=False, null=True, blank=True)
    usuario = models.ForeignKey(User, null=True, blank=True)

    def save(self):
        self.identificador = 2
        super(Empresas, self).save()

    def __unicode__(self):
        return self.nombre

    def get_fotos(self):
        fotos = FotosActividadEmpresarial.objects.filter(empresa__id = self.id)
        return fotos

    class Meta:
        verbose_name_plural = "Ficha de las Empresas rurales"

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

class MercadosCompradores(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Mercados para los compradores"

class Certificaciones(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Certificaciones"

CHOICES_SI_N0=(
            (1, 'Si'),
            (2, 'No'),
    )

class ActividadEmpresarial(models.Model):
    empresa = models.ForeignKey(Empresas)
    actividad = models.ForeignKey(ActividadesEmpresariales)
    rubro_1 = models.IntegerField(choices=CHOICES_SI_N0, null=True, blank=True)
    rubro_2 = models.IntegerField(choices=CHOICES_SI_N0, null=True, blank=True)
    rubro_3 = models.IntegerField(choices=CHOICES_SI_N0, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Actividad empresarial relacionadas a los rubros"

class MercadosRubros(models.Model):
    empresa = models.ForeignKey(Empresas)
    mercado = models.ForeignKey(Mercados)
    rubro_1 = models.IntegerField(choices=CHOICES_SI_N0, null=True, blank=True)
    rubro_2 = models.IntegerField(choices=CHOICES_SI_N0, null=True, blank=True)
    rubro_3 = models.IntegerField(choices=CHOICES_SI_N0, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Mercados de los rubros"

class CompradoresRubros(models.Model):
    empresa = models.ForeignKey(Empresas)
    mercado = models.ForeignKey(MercadosCompradores)
    rubro_1 = models.IntegerField(choices=CHOICES_SI_N0, null=True, blank=True)
    rubro_2 = models.IntegerField(choices=CHOICES_SI_N0, null=True, blank=True)
    rubro_3 = models.IntegerField(choices=CHOICES_SI_N0, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Compradores de los rubros"

class CertificacionesRubros(models.Model):
    empresa = models.ForeignKey(Empresas)
    certificaciones = models.ForeignKey(Certificaciones)
    rubro_1 = models.IntegerField(choices=CHOICES_SI_N0, null=True, blank=True)
    rubro_2 = models.IntegerField(choices=CHOICES_SI_N0, null=True, blank=True)
    rubro_3 = models.IntegerField(choices=CHOICES_SI_N0, null=True, blank=True)

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
class TemasEmpresa(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Temas de las pruebas empresariales"

class MejoraEmpresas(models.Model):
    nombre_mejora = models.CharField(max_length=200)
    empresa = models.ForeignKey(Empresas)
    fecha_prueba = models.DateField()
    tema_prueba = models.ForeignKey(TemasEmpresa)
    rubro_prueba = models.ForeignKey(Rubros)
    mercado_prueba = models.ForeignKey(Mercados)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_finalizacion = models.DateField(null=True, blank=True)
    problema = models.TextField('El problema', null=True, blank=True)
    causa = models.TextField('Análisis de causas', null=True, blank=True)
    mejorar = models.TextField('Opciones a mejorar', null=True, blank=True)
    resultados = models.TextField('Resultados esperados', null=True, blank=True)
    volumen_acopio = models.TextField('Sobre el volumen de acopio', null=True, blank=True)
    mejora_proce_calidad = models.TextField('Sobre mejora de procesamiento y calidad',
                            null=True, blank=True)
    presentacion_acceso = models.TextField('Sobre la mejora en presentación y acceso a mercado',
                            null=True, blank=True)
    inversion_credito = models.TextField('Sobre la mejora en inversión o crédito',
                        null=True, blank=True)
    mejora_precio = models.TextField('Sobre la mejora en precio o condiciones de comercialización',
                    null=True, blank=True)
    mejora_ingreso = models.TextField('Sobre la mejora en ingresos', null=True, blank=True)
    reduccion_costo = models.TextField('Sobre la reducción de costo y riesgo',
                        null=True, blank=True)

    anio = models.IntegerField(editable=False, null=True, blank=True)
    usuario = models.ForeignKey(User, null=True, blank=True)

    def save(self):
        self.anio = self.fecha_prueba.year
        super(MejoraEmpresas, self).save()

    def color_completo(self):
        if not self.resultados and not self.mejora_ingreso:
            return False
        else:
            return True
    color_completo.boolean = True
    color_completo.short_description = 'Ficha completa'

    def __unicode__(self):
        return u'%s' % (self.nombre_mejora)

    def get_fotos(self):
        fotos = FotosMejoraEmpresa.objects.filter(mejora_empresa__id = self.id)
        return fotos

    class Meta:
        verbose_name_plural = "Ficha de Mejoras de Prácticas Empresariales"


class DiasCampoEmpresa(models.Model):
    mejora_empresa = models.ForeignKey(MejoraEmpresas)
    fechas = models.DateField()
    hombres = models.IntegerField('Participantes hombres')
    mujeres = models.IntegerField('Participantes mujeres')
    comentario = models.TextField()

    def __unicode__(self):
        return 'Dias de campos de: %s' % self.mejora_empresa

    class Meta:
        verbose_name_plural = "Dias de campos de las pruebas"

class FotosMejoraEmpresa(models.Model):
    mejora_empresa = models.ForeignKey(MejoraEmpresas)
    nombre = models.CharField(max_length=200)
    foto = ImageField(upload_to=get_file_path, blank=True, null=True)

    fileDir = 'fotoMejoraEmpresa/'

    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Fotos de la mejora de prácticas empresariales"
