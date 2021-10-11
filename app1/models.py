from datetime import date
from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.

class ModeloAuditoria(models.Model):
    fecha_crea = models.DateTimeField(auto_now_add=True)
    fecha_modifica = models.DateTimeField(auto_now=True)
    ACTIVO = 'Activo'
    INACTIVO = 'Inactivo'
    ESTADO_OPCIONES = [
        (ACTIVO, 'Activo'),
        (INACTIVO, 'Inactivo'),
    ]
    estado = models.CharField(max_length=8, choices=ESTADO_OPCIONES, default=ACTIVO)

    activo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Categoria(ModeloAuditoria):
    descripcion = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.descripcion
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria,self).save()
    
    class Meta:
        verbose_name_plural = "Categorias"

class Persona(ModeloAuditoria):
    nombre = models.CharField(
        max_length=50,
    )
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateTimeField(null=False,blank=False)

    @property
    def edad(self):
        today = date.today()
        age = today.year - self.fecha_nacimiento.year - \
            ((today.month, today.day) < \
                (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        return age

    @property
    def nombre_completo(self):
        return "{} {}".format(self.nombre,self.apellido)

    def __str__(self):
        return "{} {}".format(self.nombre,self.apellido)

    def save(self):
        self.nombre = self.nombre.capitalize()
        self.apellido = self.apellido.capitalize()
        super(Persona,self).save()

    class Meta:
        verbose_name_plural = "Personas"

class Animal(ModeloAuditoria):
    nombre = models.CharField(max_length=10)
    patas = models.IntegerField(default=4)

    def __str__(self):
        return self.nombre

    def save(self):
        self.nombre = self.nombre.capitalize()
        super(Animal,self).save()

    class Meta:
        verbose_name_plural = "Animales"

class Libro(ModeloAuditoria):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField(default=1,help_text=" en dolares")
    peso = models.PositiveIntegerField(help_text=" en kilos")
    VIRTUAL = 'Virtual'
    FISICO = 'Fisico'
    TIPO_OPCIONES = [
        (VIRTUAL,'Virtual'),
        (FISICO, 'Fisico'),
    ]
    tipo = models.CharField(
        max_length=7,
        choices=TIPO_OPCIONES,
        default=FISICO,
    )
    url_download = models.URLField(default=None)

    def __str__(self):
        return "{}[{}]".format(self.nombre,self.Tipo)
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Libro,self).save()

    class Meta:
        verbose_name_plural = "libros",
        unique_together = ('nombre','tipo')