from django.db import models

# Create your models here.

class Estudiante(models.Model):
    Nombre = models.CharField(max_length=30,blank=False,null=True)
    Apellido = models.CharField(max_length=30,blank=False,null=True)
    cedula = models.CharField(primary_key=True,unique=True,max_length=10,blank=False)
    Fecha_de_naciemiento = models.DateField()
    correo = models.EmailField(unique=True,blank=False)
    Celular = models.CharField(max_length=10,null=True)
    
    def __str__(self):
        return self.cedula

class Docente(models.Model):
   Nombre = models.CharField(max_length=30,blank=False,null=True)
   Apellido = models.CharField(max_length=30,blank=False,null=True)
   cedula = models.CharField(primary_key=True,unique=True,max_length=10,blank=False)
   correo = models.EmailField(unique=True,blank=False)
   Celular = models.CharField(max_length=10,null=True)

   def __strt__(self):
       return self.cedula
   
class Materia(models.Model):
    id_materia = models.CharField(primary_key=True,unique=True,max_length=5)
    nombre = models.CharField(max_length=50)
    cedula = models.ForeignKey(Docente,on_delete=models.RESTRICT)
    
    def __str__(self):
        return self.nombre

class Nota(models.Model):
    id_nota = models.AutoField(primary_key=True)
    Estudiante = models.ForeignKey(Estudiante,on_delete=models.RESTRICT)
    Materia = models.ForeignKey(Materia,on_delete=models.RESTRICT)
    Calificacion = models.FloatField()
    
    def __float__(self):
        return self.id