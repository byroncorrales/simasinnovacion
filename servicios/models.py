#encoding: utf-8

from django.db import models
from sorl.thumbnail import ImageField
from simasinnovacion.utils import get_file_path

class OrganizacionSolicita(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Nombre de la Organización que solicita el servicio"

class OrganizacionBenefician(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Nombre de las organizaciones que benefician del servicio"

class TiposServicio(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipos de servicios"

class TemasAbordan(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Temas que abordan"

class TiposOrganizacionBenefician(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipo de organización que beneficia"

class Servicios(models.Model):
    nombre = models.CharField('Nombre de servicio', max_length=200)
    solicita_servicio = models.ForeignKey(OrganizacionSolicita)
    benefician_servicio = models.ManyToManyField(OrganizacionBenefician)
    monto = models.FloatField('Monto del servicio US$')
    tipos_servicios = models.ManyToManyField(TiposServicio)
    temas_abordan = models.ManyToManyField(TemasAbordan)
    org_benefician = models.ManyToManyField(TiposOrganizacionBenefician, 
                     verbose_name=u'Tipo de organización que beneficia')
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    objetivos = models.TextField()
    conclusiones = models.TextField('Conclusiones del servicio')
    #campo oculto
    fecha = models.IntegerField(editable=False, null=True, blank=True)

    def save(self):
        self.fecha = self.fecha_inicio.year
        super(Servicios, self).save()

    def __unicode__(self):
        return self.nombre
    def get_fotos(self):
        fotos = FotosServicios.objects.filter(servicio__id = self.id)
        return fotos

    class Meta:
        verbose_name_plural = "Ficha de Servicios para mejorar la capacidad de organizaciones"

class EvaluacionServicio(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipos de evaluación"

CHOICE_ESCALA = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    )

class ResultadoEvaluacion(models.Model):
    servicio = models.ForeignKey(Servicios)
    evaluacion = models.ForeignKey(EvaluacionServicio)
    escala = models.IntegerField(choices=CHOICE_ESCALA)

    class Meta:
        verbose_name_plural = "Resultados de evaluación de servicio por usuario"


class FotosServicios(models.Model):
    servicio = models.ForeignKey(Servicios)
    nombre = models.CharField(max_length=200)
    foto = ImageField(upload_to=get_file_path, blank=True, null=True)

    fileDir = 'fotoServicios/'

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Fotos del servicios"