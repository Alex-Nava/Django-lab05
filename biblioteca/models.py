from django.db import models

class Libro(models.Model):
    idlibro = models.AutoField(primary_key=True)  
    nombre = models.CharField(max_length=255)    
    autor = models.CharField(max_length=255)     
    publicacion = models.DateField() 
    volumen = models.IntegerField(default=0)           

    def _str_(self):
        return self.nombre


class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)  
    nombre = models.CharField(max_length=255)       
    contraseña = models.CharField(max_length=255)   
    def _str_(self):
        return self.nombre


class Review(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)  
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  
    contenido = models.TextField()  

    def _str_(self):
        return f'Review de {self.usuario.nombre} para {self.libro.nombre}'