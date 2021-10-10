from django.db import models

# Create your models here.
class Categoria(models.Model):
    descripcion = models.CharField(max_length=50, unique=True)
    fecha_crea = models.DateTimeField(auto_now_add=True)
    fecha_modifica = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.descripcion
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria,self).save()
    
    class Meta:
        verbose_name_plural = "Categorias"