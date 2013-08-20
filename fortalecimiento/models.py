#encoding: utf-8

from django.db import models
from simasinnovacion.utils import get_file_path
from sorl.thumbnail import ImageField

class TiposMedios(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipos de medios"

class TemasAbordan(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Los temas que abordan"

class GruposMetas(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Grupos metas a quien dirige"

class PapelSimas(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Papel de SIMAS en la iniciativa"

class MediosFortalecimiento(models.Model):
    nombre = models.CharField('Nombre de medio', max_length=200)
    tipo_medio = models.ManyToManyField(TiposMedios)
    temas = models.ManyToManyField(TemasAbordan)
    grupos_metas = models.ManyToManyField(GruposMetas)
    papel_simas = models.ManyToManyField(PapelSimas)
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    objetivos = models.TextField()
    #oculto
    fecha = models.IntegerField(editable=False, null=True, blank=True)

    def save(self):
        self.fecha = self.fecha_inicio.year
        super(MediosFortalecimiento, self).save()

    def __unicode__(self):
        return self.nombre

    def get_medios(self):
        return "\n,".join([medio.nombre for medio in self.tipo_medio.all()])
    get_medios.short_description = "Tipos de medios"

    def get_temas(self):
        return "\n,".join([tema.nombre for tema in self.temas.all()])
    get_temas.short_description = "Temas"

    class Meta:
        verbose_name_plural = "Ficha de Medios para fortalecimiento de conocimiento de actores"

class PersonasResultados(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Opciones de personas"

class Participantes(models.Model):
    medios = models.ForeignKey(MediosFortalecimiento)
    opcion = models.ForeignKey(PersonasResultados)
    hombres = models.IntegerField()
    mujeres = models.IntegerField()

    class Meta:
        verbose_name_plural = "Número de participantes"
CHOICE_ESCALA = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    )
class NivelConocimiento(models.Model):
    medios = models.ForeignKey(MediosFortalecimiento)
    opcion = models.ForeignKey(PersonasResultados)
    ante_evento = models.IntegerField(choices=CHOICE_ESCALA)
    despues_evento = models.IntegerField(choices=CHOICE_ESCALA)

    def __unicode__(self):
        return self.id

    class Meta:
        verbose_name_plural = "Promedio de nivel de conocimiento de participantes según auto-evaluación (escala 1-5)"

class FotosMedios(models.Model):
    medios = models.ForeignKey(MediosFortalecimiento)
    nombre = models.CharField(max_length=200)
    foto = ImageField(upload_to=get_file_path, blank=True, null=True)

    fileDir = 'fotoMediosFortalecimiento/'

    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Fotos de la actividad"
