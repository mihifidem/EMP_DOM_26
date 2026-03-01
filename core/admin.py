from django.contrib import admin
from .models import UserProfile, UsuarioNino, PuntosSeccion


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['nombre_padre', 'user_username', 'user_email']
    search_fields = ['nombre_padre', 'user__username', 'user__email']
    
    def user_username(self, obj):
        return obj.user.username
    user_username.short_description = 'Usuario'
    
    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = 'Email'


@admin.register(UsuarioNino)
class UsuarioNinoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'genero', 'fecha_nacimiento', 'user_username']
    search_fields = ['nombre', 'user__username']
    list_filter = ['genero', 'fecha_nacimiento']
    
    def user_username(self, obj):
        return obj.user.username
    user_username.short_description = 'Usuario Padre'


@admin.register(PuntosSeccion)
class PuntosSeccioAdmin(admin.ModelAdmin):
    list_display = ['nino', 'seccion', 'puntos_totales', 'get_actividades', 'fecha_actualizacion']
    search_fields = ['nino__nombre', 'seccion__titulo']
    list_filter = ['seccion', 'karaoke_completado', 'juego_completado', 'infografia_completado', 'microhistoria_completado', 'video_completado', 'tareas_completado']
    readonly_fields = ['puntos_totales', 'fecha_actualizacion', 'fecha_creacion']
    fieldsets = (
        ('Información', {
            'fields': ('nino', 'seccion')
        }),
        ('Actividades Completadas', {
            'fields': ('karaoke_completado', 'juego_completado', 'infografia_completado', 'microhistoria_completado', 'video_completado', 'tareas_completado')
        }),
        ('Puntos', {
            'fields': ('puntos_totales',)
        }),
        ('Timestamps', {
            'fields': ('fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        })
    )
    
    def get_actividades(self, obj):
        actividades = []
        if obj.karaoke_completado:
            actividades.append('🎤')
        if obj.juego_completado:
            actividades.append('🎮')
        if obj.infografia_completado:
            actividades.append('📊')
        if obj.microhistoria_completado:
            actividades.append('📖')
        if obj.video_completado:
            actividades.append('🎥')
        if obj.tareas_completado:
            actividades.append('✅')
        return ' '.join(actividades) or '-'
    get_actividades.short_description = 'Actividades'
