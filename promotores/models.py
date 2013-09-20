#encoding: utf-8

from django.db import models
from lugar.models import Departamento, Municipio
from smart_selects.db_fields import ChainedForeignKey
from geoposition.fields import GeopositionField
from sorl.thumbnail import ImageField
from simasinnovacion.utils import get_file_path
from django.contrib.auth.models import User 

CHOICE_EDUCACION = (
            (1, 'Analfabeta'),
            (2, 'Alfabetizado'),
            (3, 'Primaria incompleta'),
            (4, 'Primaria completa'),
            (5, 'Secundaria no completa'),
            (6, 'Secundaria completa'),
            (7, 'Técnico/a'),
            (8, 'Universitario/a'),
        )


#--------- modelos utiles para las fichas principales -----------
class OrganizacionCampesina(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Organizaciones campesinas"

class OrganizacionCivil(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Organizaciones civiles"

class EscuelaCampo(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Escuelas de campos"

class CultivosFinca(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Cultivos en la finca"

class AnimalesFinca(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Animales en la finca"

class ProductoProcesado(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Productos procesados"

class MercadoAcceso(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Mercados de accesos"

class TipoSuelo(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipos de suelos"
#--------------------------------------------------
        #modelo de promotor 
#--------------------------------------------------
class Promotor(models.Model):
    nombre = models.CharField(max_length=200)
    sexo = models.IntegerField(choices=((1,'Masculino'),(2, 'Femenino')))
    edad = models.IntegerField()
    educacion = models.IntegerField('Nivel de educación formal', 
                                    choices=CHOICE_EDUCACION)
    contacto = models.CharField(help_text='Número de celular', max_length=50,
                                null=True, blank=True)
    activo = models.IntegerField('Años activos en prueba de practicas', 
                                  choices=((1, '2013'),(2, '2014'),(3, '2015'),
                                           (4, '2016'),))
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
    organizacion_campesina = models.ForeignKey(OrganizacionCampesina, 
                             verbose_name=u'Nombre de organización campesina que pertenece')
    organizacion_civil = models.ForeignKey(OrganizacionCivil,
                         verbose_name=u'Nombre Organización de sociedad civil que apoya')
    escuela = models.ForeignKey(EscuelaCampo, verbose_name=u'Escuela de campo que asiste')
    tipo_suelo = models.ForeignKey(TipoSuelo)
    tipo_clima = models.IntegerField(choices=((1, 'Árido'),(2, 'Seco'),
                                              (3, 'Semi-seco'),(4, 'Semi-húmedo'),
                                              (5, 'Húmedo'),))
    meses_lluvia = models.IntegerField()
    finca = models.FloatField('Tamaño de finca en Mz')
    riego = models.IntegerField(choices=((1, 'No hay'),(2, 'Por gravedad'),
                                         (3, 'Por aspersión'),(4, 'Por goteo'),))
    bosque = models.FloatField()
    potrero = models.FloatField('Potrero con árboles')
    tacotales = models.FloatField()
    forestal = models.FloatField('Plantación forestal')
    perennes = models.FloatField('Cultivo Perennes')
    lena = models.FloatField('Plantación para leñas')
    anuales = models.FloatField('Cultivo Anuales')
    frutales = models.FloatField()
    potrero_abierto = models.FloatField('Potrero abierto')
    patio = models.FloatField()
    cultivos_finca = models.ManyToManyField(CultivosFinca)
    animales_finca = models.ManyToManyField(AnimalesFinca)
    producto_procesado = models.ManyToManyField(ProductoProcesado)
    mercado_accede = models.ManyToManyField(MercadoAcceso)

    identificador = models.IntegerField(editable=False, null=True, blank=True)
    usuario = models.ForeignKey(User, null=True, blank=True)

    def save(self):
        self.identificador = 1
        super(Promotor, self).save()

    def __unicode__(self):
        return u'%s' % (self.nombre)

    def get_fotos(self):
        fotos = FotosPromotor.objects.filter(promotor__id = self.id)
        return fotos

    class Meta:
        verbose_name_plural = 'Ficha de los promotores o promotoras' 

class FotosPromotor(models.Model):
    promotor = models.ForeignKey(Promotor)
    nombre = models.CharField(max_length=200)
    foto = ImageField(upload_to=get_file_path, blank=True, null=True)

    fileDir = 'fotoPromotor/'

    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Fotos de la familia promotor"

#---------------------------------------------------------------
            #modelo para practicas de los promotores
#---------------------------------------------------------------
class TemasPruebas(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Temas de las pruebas"

class RubroPruebas(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Rubros de las pruebas"

class EscalaPruebas(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Escalas de las pruebas"

class PracticasProductivas(models.Model):
    promotor = models.ForeignKey(Promotor)
    nombre_prueba = models.CharField(max_length=200)
    fecha_prueba = models.DateField()
    tema_prueba = models.ForeignKey(TemasPruebas)
    rubro_prueba = models.ForeignKey(RubroPruebas)
    escala_prueba = models.ForeignKey(EscalaPruebas)
    historia = models.TextField(null=True, blank=True)
    fecha_inicio = models.DateField(null=True,blank=True)
    fecha_finalizacion = models.DateField(null=True,blank=True)
    problema = models.TextField('El problema', null=True,blank=True)
    agroecologico = models.TextField('Análisis agroecológico', null=True,blank=True)
    aprobar = models.TextField('Opciones a probar', null=True,blank=True)
    resultados = models.TextField('Resultados esperados', null=True,blank=True)
    salud_planta = models.TextField('Sobre salud de las plantas', null=True,blank=True)
    vida_suelo = models.TextField('Sobre la vida de suelo', null=True,blank=True)
    prod_rendimiento = models.TextField('Sobre la producción y rendimiento', null=True,blank=True)
    calidad_producto = models.TextField('Sobre la calidad de productos', null=True,blank=True)
    plagas = models.TextField('Sobre las plagas e enfermedades', null=True,blank=True)
    costo = models.TextField('Sobre ingresos y costos', null=True,blank=True)

    #campo oculto
    anio = models.IntegerField(editable=False, null=True, blank=True)
    usuario = models.ForeignKey(User, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.anio = self.fecha_prueba.year
        super(PracticasProductivas, self).save(*args, **kwargs)

    def color_completo(self):
        if not self.resultados and not self.costo:
            return False
        else:
            return True
    color_completo.boolean = True
    color_completo.short_description = 'Ficha completa'
        
    def __unicode__(self):
        return u'%s' % (self.nombre_prueba)

    def get_fotos(self):
        fotos = FotosPrueba.objects.filter(practicas__id = self.id)
        return fotos

    class Meta:
        verbose_name_plural = "Ficha de Pruebas de Prácticas Productivas"

class DiasCampoPrueba(models.Model):
    prueba = models.ForeignKey(PracticasProductivas)
    fechas = models.DateField()
    hombres = models.IntegerField('Participantes hombres')
    mujeres = models.IntegerField('Participantes mujeres')
    comentario = models.TextField()

    def __unicode__(self):
        return 'Dias de campos de: %s' % self.prueba

    class Meta:
        verbose_name_plural = "Dias de campos de las pruebas"

class FotosPrueba(models.Model):
    practicas = models.ForeignKey(PracticasProductivas)
    nombre = models.CharField(max_length=200)
    foto = ImageField(upload_to=get_file_path, blank=True, null=True)

    fileDir = 'fotoPracticas/'

    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Fotos actividades pruebas practicas"