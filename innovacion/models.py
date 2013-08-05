#encoding: utf-8

from django.db import models
from lugar.models import Departamento, Municipio
from sorl.thumbnail import ImageField
from simasinnovacion.utils import get_file_path 

class TipoEspacio(models.Model):
	nombre = models.CharField(max_length=200)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = "Tipos de espacios"

CHOICE_COBERTURA = (
            (1, 'Regional'),
            (2, 'Nacional'),
            (3, 'Territorial'),
            (4, '7. Municipal'),
        )

class PapelSimas(models.Model):
	nombre = models.CharField(max_length=200)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = "Papel de SIMAS"

class TemasIncidencia(models.Model):
	nombre = models.CharField(max_length=200)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = "Temas principales de incidencia o innovación política"

class ActividadesEspacio(models.Model):
	nombre = models.CharField(max_length=200)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = "Actividades empresarial del espacio"

#--------------------------------------------------------------------------------------------
#                      Ficha de las Espacios de Innovación Políticas
#--------------------------------------------------------------------------------------------

class EspacioInnovacion(models.Model):
	nombre = models.CharField('Nombre del espacio', max_length=200)
	tipos = models.ForeignKey(TipoEspacio)
	activos = models.IntegerField('Años activo en innovación de políticas', 
                                  choices=((1, '2013'),(2, '2014'),(3, '2015'),
                                           (4, '2016'),))
	tiempo_formado = models.IntegerField('Años de haber formado en espacio')
	nombre = models.CharField('Nombre del contacto', max_length=200)
	celular = models.CharField(max_length=50)
	correo = models.EmailField()
	zona = models.IntegerField(choices=((1, 'Seca'),(2, 'Alta'),(3, 'Húmeda'),))
	cobertura = models.IntegerField(choices=CHOICE_COBERTURA)
	departamento_influye = models.ManyToManyField(Departamento)
	municipios_influye = models.ManyToManyField(Municipio)
	numero_entidades = models.IntegerField('Número de entidades (actores y organizaciones) que conforman el espacio') 
	papel = models.ManyToManyField(PapelSimas)
	temas = models.ManyToManyField(TemasIncidencia)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = "Ficha de las Espacios de Innovación Políticas"


class ActividadEmpresarial(models.Model):
    espacio = models.ForeignKey(EspacioInnovacion)
    actividad = models.ForeignKey(ActividadesEspacio)
    tema_1 = models.ForeignKey(TemasIncidencia, related_name="act_temauno", null=True, blank=True)
    tema_2 = models.ForeignKey(TemasIncidencia, related_name="act_temados", null=True, blank=True)
    tema_3 = models.ForeignKey(TemasIncidencia, related_name="act_tematres", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Actividad empresarial relacionadas a los rubros"

class FotosInnovacion(models.Model):
    espacio = models.ForeignKey(EspacioInnovacion)
    nombre = models.CharField(max_length=200)
    foto = ImageField(upload_to=get_file_path, blank=True, null=True)

    fileDir = 'fotoInnovacion/'

    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Fotos de las actividades de iniciativa de innovación política"

#--------------------------------------------------------------------------------------------
#                       Ficha de Iniciativas de innovación de políticas
#--------------------------------------------------------------------------------------------
class TipoIniciativa(models.Model):
	nombre = models.CharField(max_length=200)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = "Tipos de iniciativas"

class TemasAborda(models.Model):
	nombre = models.CharField(max_length=200)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = "Los temas que aborda la iniciativa"

class ActividadIniciativa(models.Model):
	nombre = models.CharField(max_length=200)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = "Las actividades que contempla la iniciativa"

class IniciativaInnovacion(models.Model):
	nombre = models.CharField('Nombre de la iniciativa', max_length=200)
	espacio = models.ForeignKey(EspacioInnovacion)
	tipo = models.ForeignKey(TipoIniciativa, verbose_name="Tipo de iniciativa")
	fecha_inicio = models.DateField()
	fecha_finalizacion = models.DateField()
	temas = models.ManyToManyField(TemasAborda)
	actividades = models.ManyToManyField(ActividadIniciativa)
	problema = models.TextField('El problema')
	analisis = models.TextField('Análisis de tema')
	enfoque = models.TextField('Enfoque de la iniciativa')
	resultado = models.TextField('Resultados esperados')
	sobre_tierra  = models.TextField('Sobre la defensa de tierra')
	fomento = models.TextField('Sobre el fomento de producción agroecológica y alimentos sanos')
	conservacion = models.TextField('Sobre la conservación de recursos naturales, semilla criolla y biodiversidad')
	inversion = models.TextField('Sobre la mejora en inversión pública, privada  o acceso a crédito')
	acceso_mercado = models.TextField('Sobre la mejora en acceso a mercados locales para los alimentos')
	comunicacion = models.TextField('Sobre la mejora en comunicación y desarrollo de protagonismo de pequeños produtores')
	reduccion = models.TextField('Sobre la reducción de riesgo de los sistemas locales de alimentos')

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = "Ficha de Iniciativas de innovación de políticas"

class FotosIniciativa(models.Model):
    iniciativa = models.ForeignKey(IniciativaInnovacion)
    nombre = models.CharField(max_length=200)
    foto = ImageField(upload_to=get_file_path, blank=True, null=True)

    fileDir = 'fotoIniciativa/'

    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Fotos de las actividades de la iniciativa de innovación política"