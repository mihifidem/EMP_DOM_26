from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	nombre_padre = models.CharField(max_length=150)

	def __str__(self):
		return f"{self.nombre_padre} ({self.user.username})"


class UsuarioNino(models.Model):
	GENERO_CHOICES = [
		('M', 'Masculino'),
		('F', 'Femenino'),
		('O', 'Otro'),
	]

	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ninos')
	nombre = models.CharField(max_length=100)
	genero = models.CharField(max_length=1, choices=GENERO_CHOICES, blank=True, null=True)
	fecha_nacimiento = models.DateField(blank=True, null=True)

	def __str__(self):
		return f"{self.nombre}"

	class Meta:
		verbose_name = "Usuario Nino"
		verbose_name_plural = "Usuarios Ninos"
		ordering = ['user', 'nombre']

class PuntosSeccion(models.Model):
	"""Modelo para controlar los puntos ganados por actividades en cada sección"""
	nino = models.ForeignKey(UsuarioNino, on_delete=models.CASCADE, related_name='puntos_secciones')
	seccion = models.ForeignKey('books.Section', on_delete=models.CASCADE, related_name='puntos_ninos')
	
	# Actividades completadas (Boolean para marcar si ya se ganaron puntos)
	karaoke_completado = models.BooleanField(default=False)
	juego_completado = models.BooleanField(default=False)
	infografia_completado = models.BooleanField(default=False)
	microhistoria_completado = models.BooleanField(default=False)
	video_completado = models.BooleanField(default=False)
	tareas_completado = models.BooleanField(default=False)
	
	# Puntos totales (1 punto por cada actividad completada)
	puntos_totales = models.IntegerField(default=0)
	fecha_actualizacion = models.DateTimeField(auto_now=True)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	
	def calcular_puntos(self):
		"""Calcula los puntos totales basado en las actividades completadas"""
		self.puntos_totales = sum([
			self.karaoke_completado,
			self.juego_completado,
			self.infografia_completado,
			self.microhistoria_completado,
			self.video_completado,
			self.tareas_completado
		])
		self.save()
		return self.puntos_totales
	
	def __str__(self):
		return f"{self.nino.nombre} - Sección {self.seccion.id}: {self.puntos_totales} puntos"
	
	class Meta:
		unique_together = ('nino', 'seccion')
		ordering = ['-fecha_actualizacion']
		verbose_name = "Puntos por Sección"
		verbose_name_plural = "Puntos por Sección"