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
    COLORES_CARD = [
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
    
    libro = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='secciones')
    numero = models.IntegerField(help_text="Número de sección en el libro")
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    numero_pagina_inicio = models.IntegerField(blank=True, null=True)
    numero_pagina_fin = models.IntegerField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    color_card = models.CharField(max_length=20, choices=COLORES_CARD, default='azul', help_text="Color del gradiente de la tarjeta")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.libro.titulo} - Sección {self.numero}: {self.titulo}"
    
    def get_color_gradient(self):
        """Retorna el gradiente CSS según el color seleccionado"""
        gradientes = {
            'azul': 'linear-gradient(135deg, #48c6ef 0%, #6f86d6 100%)',
            'violeta': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
            'verde': 'linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%)',
            'naranja': 'linear-gradient(135deg, #fa709a 0%, #fee140 100%)',
            'rosa': 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
            'turquesa': 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
            'indigo': 'linear-gradient(135deg, #7f7fd5 0%, #86a8e7 100%)',
            'rojo': 'linear-gradient(135deg, #fa709a 0%, #fee140 100%)',
        }
        return gradientes.get(self.color_card, gradientes['azul'])
    
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
