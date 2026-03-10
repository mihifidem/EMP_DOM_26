from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    """Modelo para Autores"""
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    biografia = models.TextField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    pais = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    class Meta:
        ordering = ['apellido', 'nombre']
        verbose_name = "Autor"
        verbose_name_plural = "Autores"


class Category(models.Model):
    """Modelo para Categorías de Libros"""
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['nombre']


class Publisher(models.Model):
    """Modelo para Editoriales"""
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    pais = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ['nombre']
        verbose_name = "Editorial"
        verbose_name_plural = "Editoriales"


class ColorCard(models.Model):
    """Modelo para gestionar colores de tarjetas con propiedades litúrgicas"""
    COLORES_CHOICES = [
        ('azul', 'Azul'),
        ('violeta', 'Violeta'),
        ('verde', 'Verde'),
        ('naranja', 'Naranja'),
        ('rosa', 'Rosa'),
        ('turquesa', 'Turquesa'),
        ('indigo', 'Índigo'),
        ('rojo', 'Rojo'),
        ('blanco', 'Blanco'),
    ]
    
    nombre = models.CharField(max_length=20, choices=COLORES_CHOICES, unique=True)
    display_name = models.CharField(max_length=50)
    gradiente_css = models.CharField(max_length=200, help_text="Gradiente CSS del color")
    es_liturgico = models.BooleanField(default=False, help_text="Indica si es un color litúrgico")
    descripcion_liturgica = models.CharField(max_length=200, blank=True, null=True, help_text="Significado litúrgico del color")
    
    def __str__(self):
        return f"{self.display_name}{'  [LITÚRGICO]' if self.es_liturgico else ''}"
    
    class Meta:
        ordering = ['nombre']
        verbose_name = "Color de Tarjeta"
        verbose_name_plural = "Colores de Tarjeta"


class Book(models.Model):
    """Modelo para Libros"""
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='libros')
    categoria = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='libros')
    editorial = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True, blank=True, related_name='libros')
    
    isbn = models.CharField(max_length=13, unique=True, blank=True, null=True)
    descripcion = models.TextField()
    fecha_publicacion = models.DateField()
    numero_paginas = models.IntegerField(blank=True, null=True)
    idioma = models.CharField(max_length=20, default='Español')
    
    portada = models.ImageField(upload_to='books/covers/', blank=True, null=True)
    pdf = models.FileField(upload_to='books/pdfs/', blank=True, null=True)
    
    calificacion = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    disponible = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.titulo} - {self.autor}"
    
    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        indexes = [
            models.Index(fields=['titulo']),
            models.Index(fields=['autor']),
            models.Index(fields=['categoria']),
        ]


class Section(models.Model):
    """Modelo para Secciones dentro de un Libro"""
    libro = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='secciones')
    numero = models.IntegerField(help_text="Número de sección en el libro")
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    numero_pagina_inicio = models.IntegerField(blank=True, null=True)
    numero_pagina_fin = models.IntegerField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    color_card = models.ForeignKey(ColorCard, on_delete=models.SET_NULL, null=True, default=None, related_name='secciones', help_text="Color del gradiente de la tarjeta")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.libro.titulo} - Sección {self.numero}: {self.titulo}"
    
    def get_color_gradient(self):
        """Retorna el gradiente CSS según el color seleccionado"""
        if self.color_card:
            return self.color_card.gradiente_css
        return 'linear-gradient(135deg, #48c6ef 0%, #6f86d6 100%)'  # Azul por defecto
    
    class Meta:
        ordering = ['libro', 'numero']
        verbose_name = "Sección"
        verbose_name_plural = "Secciones"
        unique_together = ['libro', 'numero']


class Tarea(models.Model):
    """Modelo para Tareas dentro de una Sección"""
    seccion = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='tareas')
    numero = models.IntegerField(help_text="Número de tarea en la sección")
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    tipo = models.CharField(
        max_length=50,
        choices=[
            ('lectura', 'Lectura'),
            ('ejercicio', 'Ejercicio'),
            ('juego', 'Juego'),
            ('video', 'Video'),
            ('otro', 'Otro'),
        ],
        default='ejercicio'
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.seccion.libro.titulo} - Sección {self.seccion.numero} - Tarea {self.numero}: {self.titulo}"
    
    class Meta:
        ordering = ['seccion', 'numero']
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
        unique_together = ['seccion', 'numero']


class TareaNino(models.Model):
    """Modelo para registrar qué niño completó qué tarea y cuándo"""
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tareas_ninos')
    nino = models.ForeignKey('core.UsuarioNino', on_delete=models.CASCADE, related_name='tareas_completadas')
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='completadas_por')
    completada = models.BooleanField(default=False)
    fecha_completado = models.DateTimeField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        estado = "✓ Completada" if self.completada else "○ Pendiente"
        return f"{self.nino.nombre} - {self.tarea.titulo} ({estado})"
    
    class Meta:
        ordering = ['-fecha_completado', 'nino', 'tarea']
        verbose_name = "Tarea del Niño"
        verbose_name_plural = "Tareas de los Niños"
        unique_together = ['nino', 'tarea']  # Un niño puede completar una tarea solo una vez
