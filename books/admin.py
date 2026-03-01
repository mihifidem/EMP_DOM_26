from django.contrib import admin
from .models import Author, Category, Publisher, Book, Section, Tarea, TareaNino


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'pais', 'fecha_nacimiento']
    search_fields = ['nombre', 'apellido']
    list_filter = ['pais', 'fecha_nacimiento']
    fieldsets = (
        ('Información Personal', {
            'fields': ('nombre', 'apellido', 'fecha_nacimiento', 'pais')
        }),
        ('Biografía', {
            'fields': ('biografia',),
            'classes': ('collapse',)
        }),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']
    fieldsets = (
        ('Información', {
            'fields': ('nombre', 'descripcion')
        }),
    )


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'ciudad', 'pais']
    search_fields = ['nombre', 'ciudad']
    list_filter = ['pais']
    fieldsets = (
        ('Editorial', {
            'fields': ('nombre', 'ciudad', 'pais')
        }),
    )


class SectionInline(admin.TabularInline):
    model = Section
    extra = 1
    fields = ('numero', 'titulo', 'numero_pagina_inicio', 'numero_pagina_fin')


class TareaInline(admin.TabularInline):
    model = Tarea
    extra = 1
    fields = ('numero', 'titulo', 'tipo')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'categoria', 'editorial', 'fecha_publicacion', 'disponible', 'calificacion']
    search_fields = ['titulo', 'autor__nombre', 'autor__apellido', 'isbn']
    list_filter = ['categoria', 'editorial', 'disponible', 'fecha_publicacion', 'idioma']
    readonly_fields = ['fecha_creacion', 'fecha_actualizacion']
    date_hierarchy = 'fecha_publicacion'
    inlines = [SectionInline]
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('titulo', 'autor', 'categoria', 'editorial')
        }),
        ('Detalles', {
            'fields': ('isbn', 'descripcion', 'fecha_publicacion', 'numero_paginas', 'idioma')
        }),
        ('Multimedia', {
            'fields': ('portada', 'pdf')
        }),
        ('Estado', {
            'fields': ('disponible', 'calificacion')
        }),
        ('Timestamps', {
            'fields': ('fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['libro', 'numero', 'titulo', 'fecha_fin', 'color_card']
    search_fields = ['titulo', 'libro__titulo']
    list_filter = ['libro', 'fecha_creacion', 'fecha_inicio', 'fecha_fin', 'color_card']
    ordering = ['libro', 'numero']
    inlines = [TareaInline]
    
    fieldsets = (
        ('Información', {
            'fields': ('libro', 'numero', 'titulo', 'color_card')
        }),
        ('Contenido', {
            'fields': ('contenido',)
        }),
        ('Paginación', {
            'fields': ('numero_pagina_inicio', 'numero_pagina_fin'),
            'classes': ('collapse',)
        }),
        ('Fechas', {
            'fields': ('fecha_inicio', 'fecha_fin')
        }),
        ('Timestamps', {
            'fields': ('fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['fecha_creacion', 'fecha_actualizacion']


@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ['seccion', 'numero', 'titulo', 'tipo', 'fecha_creacion']
    search_fields = ['titulo', 'descripcion', 'seccion__titulo', 'seccion__libro__titulo']
    list_filter = ['tipo', 'seccion__libro', 'fecha_creacion']
    ordering = ['seccion', 'numero']
    
    fieldsets = (
        ('Información', {
            'fields': ('seccion', 'numero', 'titulo', 'tipo')
        }),
        ('Contenido', {
            'fields': ('descripcion',)
        }),
        ('Timestamps', {
            'fields': ('fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['fecha_creacion', 'fecha_actualizacion']


@admin.register(TareaNino)
class TareaNinoAdmin(admin.ModelAdmin):
    list_display = ['nino', 'tarea', 'completada', 'fecha_completado', 'usuario']
    search_fields = ['nino__nombre', 'tarea__titulo', 'usuario__username']
    list_filter = ['completada', 'fecha_completado', 'tarea__tipo']
    ordering = ['-fecha_completado', 'nino']
    
    def get_usuario_username(self, obj):
        return obj.usuario.username
    get_usuario_username.short_description = 'Usuario'
    
    fieldsets = (
        ('Información', {
            'fields': ('usuario', 'nino', 'tarea')
        }),
        ('Estado', {
            'fields': ('completada', 'fecha_completado')
        }),
        ('Timestamps', {
            'fields': ('fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['fecha_creacion', 'fecha_actualizacion']
