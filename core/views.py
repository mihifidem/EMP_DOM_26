# --- IMPORTS ---
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.http import require_POST
from .forms import RegisterForm, UsuarioNinoForm
from .models import UsuarioNino, PuntosSeccion
from books.models import Section, Tarea, TareaNino

# --- FUNCIONES HELPER ---

def registrar_actividad_completada(nino, seccion_id, actividad):
	"""
	Registra que un niño completó una actividad en una sección y devuelve los puntos totales.
	
	Args:
		nino: Instancia de UsuarioNino
		seccion_id: ID de la sección
		actividad: Tipo de actividad ('karaoke', 'juego', 'infografia', 'microhistoria', 'video', 'tareas')
	
	Returns:
		dict con 'puntos_totales' y 'mensaje'
	"""
	try:
		seccion = Section.objects.get(id=seccion_id)
		puntos_seccion, created = PuntosSeccion.objects.get_or_create(nino=nino, seccion=seccion)
		
		# Mapeo de actividad a campo del modelo
		campos_actividad = {
			'karaoke': 'karaoke_completado',
			'juego': 'juego_completado',
			'infografia': 'infografia_completado',
			'microhistoria': 'microhistoria_completado',
			'video': 'video_completado',
			'tareas': 'tareas_completado'
		}
		
		if actividad not in campos_actividad:
			return {'puntos_totales': puntos_seccion.puntos_totales, 'error': 'Actividad no reconocida'}
		
		campo = campos_actividad[actividad]
		
		# Verificar si ya estaba completada
		ya_completada = getattr(puntos_seccion, campo)
		
		# Marcar como completada
		setattr(puntos_seccion, campo, True)
		puntos_seccion.calcular_puntos()
		
		mensaje = f"¡Actividad '{actividad}' marcada como completada!" if not ya_completada else "Actividad ya estaba completada"
		
		return {
			'puntos_totales': puntos_seccion.puntos_totales,
			'mensaje': mensaje,
			'nueva_actividad': not ya_completada
		}
	except Section.DoesNotExist:
		return {'error': 'Sección no encontrada', 'puntos_totales': 0}
	except Exception as e:
		return {'error': str(e), 'puntos_totales': 0}


def obtener_puntos_totales_nino(nino):
	"""Obtiene los puntos totales acumulados de un niño en todas las secciones"""
	puntos_secciones = PuntosSeccion.objects.filter(nino=nino)
	return sum(ps.puntos_totales for ps in puntos_secciones)

# Vista protegida para /domingo/1

@login_required
def domingo1_canciones(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    seccion_titulo = 'I Domingo de Adviento'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 1, 'canciones')
        seccion = Section.objects.get(id=1)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Canciones",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Canciones", 'url': None},
        ]
    }
    return render(request, 'domingos/01/canciones.html', context)


@login_required
def domingo1_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    seccion_titulo = 'I Domingo de Adviento'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 1, 'infografia')
        seccion = Section.objects.get(id=1)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Infografía",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Infografía", 'url': None},
        ]
    }
    return render(request, 'domingos/01/infografia.html', context)

@login_required
def domingo2_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    seccion_titulo = 'I Domingo de Adviento'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 2, 'infografia')
        seccion = Section.objects.get(id=1)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Infografía",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Infografía", 'url': None},
        ]
    }
    return render(request, 'domingos/02/infografia.html', context)


@login_required
def domingo3_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    seccion_titulo = 'III Domingo de Adviento'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 3, 'infografia')
        seccion = Section.objects.get(id=3)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Infografía",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Infografía", 'url': None},
        ]
    }
    return render(request, 'domingos/03/infografia.html', context)


@login_required
def domingo4_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    seccion_titulo = 'I Domingo de Adviento'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 4, 'infografia')
        seccion = Section.objects.get(id=4)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Infografía",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Infografía", 'url': None},
        ]
    }
    return render(request, 'domingos/04/infografia.html', context)
# Landing page
def landing(request):
    # if request.user.is_authenticated:
    #     return redirect('dashboard')
    return render(request, 'landing.html')

@login_required
def domingo5_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 4, 'infografia')
        seccion = Section.objects.get(id=4)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Infografía",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Infografía", 'url': None},
        ]
    }
    return render(request, 'domingos/05/infografia.html', context)


@login_required
def domingo6_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    seccion_titulo = 'Sagrada Familia'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 6, 'infografia')
        seccion = Section.objects.get(id=7)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Infografía",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Infografía", 'url': None},
        ]
    }
    return render(request, 'domingos/06/infografia.html', context)


@login_required
def domingo7_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    seccion_titulo = 'Epifanía'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 7, 'infografia')
        seccion = Section.objects.get(id=7)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Infografía",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Infografía", 'url': None},
        ]
    }
    return render(request, 'domingos/07/infografia.html', context)


@login_required
def domingo8_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    seccion_titulo = 'Bautismo de Jesús'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 7, 'infografia')
        seccion = Section.objects.get(id=7)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Infografía",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Infografía", 'url': None},
        ]
    }
    return render(request, 'domingos/08/infografia.html', context)


@login_required
def domingo9_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    seccion_titulo = 'Jesús crecía con sabiduría'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 8, 'infografia')
        seccion = Section.objects.get(id=8)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Infografía",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Infografía", 'url': None},
        ]
    }
    return render(request, 'domingos/09/infografia.html', context)


@login_required
def domingo10_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    seccion_titulo = 'Conversión'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 9, 'infografia')
        seccion = Section.objects.get(id=9)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Infografía",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Infografía", 'url': None},
        ]
    }
    return render(request, 'domingos/10/infografia.html', context)


@login_required
def domingo11_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    seccion_titulo = 'Candelaria'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 10, 'infografia')
        seccion = Section.objects.get(id=10)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Infografía",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Infografía", 'url': None},
        ]
    }
    return render(request, 'domingos/11/infografia.html', context)


@login_required
def domingo12_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    seccion_titulo = 'Confianza'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 11, 'infografia')
        seccion = Section.objects.get(id=11)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Infografía",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Infografía", 'url': None},
        ]
    }
    return render(request, 'domingos/12/infografia.html', context)


@login_required
def domingo13_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 12, 'infografia')
        seccion = Section.objects.get(id=12)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Infografía",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Infografía", 'url': None},
        ]
    }
    return render(request, 'domingos/13/infografia.html', context)


@login_required
def domingo14_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 13, 'infografia')
        seccion = Section.objects.get(id=13)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Infografía",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Infografía", 'url': None},
        ]
    }
    return render(request, 'domingos/14/infografia.html', context)


@login_required
def domingo15_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 14, 'infografia')
        seccion = Section.objects.get(id=14)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Infografía",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Infografía", 'url': None},
        ]
    }
    return render(request, 'domingos/15/infografia.html', context)
@login_required
def domingo16_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 15, 'infografia')
        seccion = Section.objects.get(id=15)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/16/infografia.html', context)
@login_required
def domingo17_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 16, 'infografia')
        seccion = Section.objects.get(id=16)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/17/infografia.html', context)
@login_required
def domingo18_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 17, 'infografia')
        seccion = Section.objects.get(id=17)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/18/infografia.html', context)
@login_required
def domingo19_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 18, 'infografia')
        seccion = Section.objects.get(id=18)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/19/infografia.html', context)
@login_required
def domingo20_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 19, 'infografia')
        seccion = Section.objects.get(id=19)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/20/infografia.html', context)
@login_required
def domingo21_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 20, 'infografia')
        seccion = Section.objects.get(id=20)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/21/infografia.html', context)
@login_required
def domingo22_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 21, 'infografia')
        seccion = Section.objects.get(id=21)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/22/infografia.html', context)
@login_required
def domingo23_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 22, 'infografia')
        seccion = Section.objects.get(id=22)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/23/infografia.html', context)
@login_required
def domingo24_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 23, 'infografia')
        seccion = Section.objects.get(id=23)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/24/infografia.html', context)
@login_required
def domingo25_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 24, 'infografia')
        seccion = Section.objects.get(id=24)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/25/infografia.html', context)
@login_required
def domingo26_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 25, 'infografia')
        seccion = Section.objects.get(id=25)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/26/infografia.html', context)
@login_required
def domingo27_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 26, 'infografia')
        seccion = Section.objects.get(id=26)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/27/infografia.html', context)
@login_required
def domingo28_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 27, 'infografia')
        seccion = Section.objects.get(id=27)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/28/infografia.html', context)
@login_required
def domingo29_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 28, 'infografia')
        seccion = Section.objects.get(id=28)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/29/infografia.html', context)
@login_required
def domingo30_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 29, 'infografia')
        seccion = Section.objects.get(id=29)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/30/infografia.html', context)
@login_required
def domingo31_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 30, 'infografia')
        seccion = Section.objects.get(id=30)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/31/infografia.html', context)
@login_required
def domingo32_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 31, 'infografia')
        seccion = Section.objects.get(id=31)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/32/infografia.html', context)
@login_required
def domingo33_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 32, 'infografia')
        seccion = Section.objects.get(id=32)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/33/infografia.html', context)
@login_required
def domingo34_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 33, 'infografia')
        seccion = Section.objects.get(id=33)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/34/infografia.html', context)
@login_required
def domingo35_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 34, 'infografia')
        seccion = Section.objects.get(id=34)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/35/infografia.html', context)
@login_required
def domingo36_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 35, 'infografia')
        seccion = Section.objects.get(id=35)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/36/infografia.html', context)
@login_required
def domingo37_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 36, 'infografia')
        seccion = Section.objects.get(id=36)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/37/infografia.html', context)
@login_required
def domingo38_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 37, 'infografia')
        seccion = Section.objects.get(id=37)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/38/infografia.html', context)
@login_required
def domingo39_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 38, 'infografia')
        seccion = Section.objects.get(id=38)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/39/infografia.html', context)
@login_required
def domingo40_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 39, 'infografia')
        seccion = Section.objects.get(id=39)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/40/infografia.html', context)
@login_required
def domingo41_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 40, 'infografia')
        seccion = Section.objects.get(id=40)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/41/infografia.html', context)
@login_required
def domingo42_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 41, 'infografia')
        seccion = Section.objects.get(id=41)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/42/infografia.html', context)
@login_required
def domingo43_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 42, 'infografia')
        seccion = Section.objects.get(id=42)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/43/infografia.html', context)
@login_required
def domingo44_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 43, 'infografia')
        seccion = Section.objects.get(id=43)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/44/infografia.html', context)
@login_required
def domingo45_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 44, 'infografia')
        seccion = Section.objects.get(id=44)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/45/infografia.html', context)
@login_required
def domingo46_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 45, 'infografia')
        seccion = Section.objects.get(id=45)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/46/infografia.html', context)
@login_required
def domingo47_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 46, 'infografia')
        seccion = Section.objects.get(id=46)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/47/infografia.html', context)
@login_required
def domingo48_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 47, 'infografia')
        seccion = Section.objects.get(id=47)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/48/infografia.html', context)
@login_required
def domingo49_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 48, 'infografia')
        seccion = Section.objects.get(id=48)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/49/infografia.html', context)
@login_required
def domingo50_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 49, 'infografia')
        seccion = Section.objects.get(id=49)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/50/infografia.html', context)
@login_required
def domingo51_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 50, 'infografia')
        seccion = Section.objects.get(id=50)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/51/infografia.html', context)
@login_required
def domingo52_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'NiÃ±o')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 51, 'infografia')
        seccion = Section.objects.get(id=51)
        seccion_titulo = seccion.titulo
    except:
        pass
    
    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - InfografÃ­a",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - InfografÃ­a", 'url': None},
        ]
    }
    return render(request, 'domingos/52/infografia.html', context)



# Landing page
def landing(request):
    # if request.user.is_authenticated:
    #     return redirect('dashboard')
    return render(request, 'landing.html')


@login_required
def domingo1_microhistoria(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 2, 'microhistoria')
    except:
        pass
    seccion_titulo = 'I Domingo de Adviento'

    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Microhistoria",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Microhistoria", 'url': None},
        ]
    }
    return render(request, 'domingos/01/microhistoria.html', context)


@login_required
def domingo2_microhistoria(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 1, 'microhistoria')
    except:
        pass
    seccion_titulo = 'I Domingo de Adviento'

    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Microhistoria",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Microhistoria", 'url': None},
        ]
    }
    return render(request, 'domingos/02/microhistoria.html', context)

@login_required
def domingo3_microhistoria(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 3, 'microhistoria')
    except:
        pass
    seccion_titulo = 'III Domingo de Adviento'

    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Microhistoria",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Microhistoria", 'url': None},
        ]
    }
    return render(request, 'domingos/03/microhistoria.html', context)


@login_required
def domingo4_microhistoria(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 4, 'microhistoria')
    except:
        pass
    seccion_titulo = 'IV Domingo de Adviento'

    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Microhistoria",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Microhistoria", 'url': None},
        ]
    }
    return render(request, 'domingos/04/microhistoria.html', context)

@login_required
def domingo5_microhistoria(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 5, 'microhistoria')
    except:
        pass
    seccion_titulo = 'Navidad'

    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Microhistoria",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Microhistoria", 'url': None},
        ]
    }
    return render(request, 'domingos/05/microhistoria.html', context)


@login_required
def domingo6_microhistoria(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    seccion = Section.objects.get(id=7)
    seccion_titulo = seccion.titulo
    # Registrar actividad
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 6, 'microhistoria')
    except:
        pass
  

    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Microhistoria",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Microhistoria", 'url': None},
        ]
    }
    return render(request, 'domingos/06/microhistoria.html', context)


@login_required
def domingo7_microhistoria(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 7, 'microhistoria')
    except:
        pass
    seccion_titulo = 'Epifanía'

    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Microhistoria",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Microhistoria", 'url': None},
        ]
    }
    return render(request, 'domingos/07/microhistoria.html', context)


@login_required
def domingo8_microhistoria(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 8, 'microhistoria')
    except:
        pass
    seccion_titulo = 'Bautismo de Jesús'

    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Microhistoria",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Microhistoria", 'url': None},
        ]
    }
    return render(request, 'domingos/08/microhistoria.html', context)


@login_required
def domingo9_microhistoria(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 9, 'microhistoria')
    except:
        pass
    seccion_titulo = 'Jesús crecía con sabiduría'

    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Microhistoria",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Microhistoria", 'url': None},
        ]
    }
    return render(request, 'domingos/09/microhistoria.html', context)


@login_required
def domingo10_microhistoria(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 10, 'microhistoria')
    except:
        pass
    seccion_titulo = 'Conversión'

    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Microhistoria",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Microhistoria", 'url': None},
        ]
    }
    return render(request, 'domingos/10/microhistoria.html', context)


@login_required
def domingo11_microhistoria(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 11, 'microhistoria')
    except:
        pass
    seccion_titulo = 'Candelaria'

    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Microhistoria",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Microhistoria", 'url': None},
        ]
    }
    return render(request, 'domingos/11/microhistoria.html', context)


@login_required
def domingo12_microhistoria(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 12, 'microhistoria')
    except:
        pass
    seccion_titulo = 'Confianza'

    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Microhistoria",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Microhistoria", 'url': None},
        ]
    }
    return render(request, 'domingos/12/microhistoria.html', context)


@login_required
def domingo13_microhistoria(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 13, 'microhistoria')
    except:
        pass
    seccion_titulo = 'IV Domingo de Adviento'

    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Microhistoria",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Microhistoria", 'url': None},
        ]
    }
    return render(request, 'domingos/13/microhistoria.html', context)


@login_required
def domingo14_microhistoria(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 14, 'microhistoria')
    except:
        pass
    seccion_titulo = 'IV Domingo de Adviento'

    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Microhistoria",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Microhistoria", 'url': None},
        ]
    }
    return render(request, 'domingos/14/microhistoria.html', context)


@login_required
def domingo15_microhistoria(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 15, 'microhistoria')
    except:
        pass
    seccion_titulo = 'IV Domingo de Adviento'

    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Microhistoria",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Microhistoria", 'url': None},
        ]
    }
    return render(request, 'domingos/15/microhistoria.html', context)


@login_required
def domingo1_game(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 1, 'juego')
    except:
        pass
    
    return render(request, 'domingos/01/memory.html', {'nino_nombre': nino_nombre})

@login_required
def domingo1_karaoke(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 1, 'karaoke')
    except:
        pass
    seccion_titulo = 'I Domingo de Adviento'

    puntos_totales = obtener_puntos_totales_nino(nino)
    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Karaoke",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Karaoke", 'url': None},
        ]
    }
    return render(request, 'domingos/01/karaoke.html', context)


@login_required
def domingo2_canciones(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')

    seccion_titulo = 'II Domingo de Adviento'
    puntos_totales = 0
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 2, 'canciones')
        puntos_totales = obtener_puntos_totales_nino(nino)
        seccion = Section.objects.get(id=2)
        seccion_titulo = seccion.titulo
    except:
        pass

    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Canciones",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Canciones", 'url': None},
        ]
    }
    return render(request, 'domingos/02/canciones.html', context)


@login_required
def domingo2_game(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')

    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 2, 'juego')
    except:
        pass

    return render(request, 'domingos/01/memory.html', {'nino_nombre': nino_nombre})


@login_required
def domingo2_karaoke(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')

    seccion_titulo = 'II Domingo de Adviento'
    puntos_totales = 0
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 2, 'karaoke')
        puntos_totales = obtener_puntos_totales_nino(nino)
        seccion = Section.objects.get(id=2)
        seccion_titulo = seccion.titulo
    except:
        pass

    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Karaoke",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Karaoke", 'url': None},
        ]
    }
    return render(request, 'domingos/02/karaoke.html', context)



@login_required
def domingo3_karaoke(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')

    seccion_titulo = 'III Domingo de Adviento'
    puntos_totales = 0
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 2, 'karaoke')
        puntos_totales = obtener_puntos_totales_nino(nino)
        seccion = Section.objects.get(id=2)
        seccion_titulo = seccion.titulo
    except:
        pass

    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Karaoke",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Karaoke", 'url': None},
        ]
    }
    return render(request, 'domingos/03/karaoke.html', context)


@login_required
def domingo4_karaoke(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')

    seccion_titulo = 'IV Domingo de Adviento'
    puntos_totales = 0
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 2, 'karaoke')
        puntos_totales = obtener_puntos_totales_nino(nino)
        seccion = Section.objects.get(id=2)
        seccion_titulo = seccion.titulo
    except:
        pass

    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Karaoke",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Karaoke", 'url': None},
        ]
    }
    return render(request, 'domingos/04/karaoke.html', context)


@login_required
def domingo5_karaoke(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')

    seccion_titulo = 'Navidad'
    puntos_totales = 0
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 2, 'karaoke')
        puntos_totales = obtener_puntos_totales_nino(nino)
        seccion = Section.objects.get(id=2)
        seccion_titulo = seccion.titulo
    except:
        pass

    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Karaoke",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Karaoke", 'url': None},
        ]
    }
    return render(request, 'domingos/05/karaoke.html', context)

@login_required
def domingo6_karaoke(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')

    puntos_totales = 0
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 6, 'karaoke')
        puntos_totales = obtener_puntos_totales_nino(nino)
        seccion = Section.objects.get(id=7)
        seccion_titulo = seccion.titulo
    except:
        pass

    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Karaoke",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Karaoke", 'url': None},
        ]
    }
    return render(request, 'domingos/06/karaoke.html', context)

@login_required
def domingo7_karaoke(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')

    seccion_titulo = 'Epifanía'
    puntos_totales = 0
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 7, 'karaoke')
        puntos_totales = obtener_puntos_totales_nino(nino)
        seccion = Section.objects.get(id=7)
        seccion_titulo = seccion.titulo
    except:
        pass

    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Karaoke",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Karaoke", 'url': None},
        ]
    }
    return render(request, 'domingos/07/karaoke.html', context)

@login_required
def domingo8_karaoke(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')

    seccion_titulo = 'Bautismo de Jesús'
    puntos_totales = 0
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 8, 'karaoke')
        puntos_totales = obtener_puntos_totales_nino(nino)
        seccion = Section.objects.get(id=8)
        seccion_titulo = seccion.titulo
    except:
        pass

    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Karaoke",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Karaoke", 'url': None},
        ]
    }
    return render(request, 'domingos/08/karaoke.html', context)

@login_required
def domingo9_karaoke(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')

    seccion_titulo = 'Jesús crecía con sabiduría'
    puntos_totales = 0
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 9, 'karaoke')
        puntos_totales = obtener_puntos_totales_nino(nino)
        seccion = Section.objects.get(id=9)
        seccion_titulo = seccion.titulo
    except:
        pass

    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Karaoke",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Karaoke", 'url': None},
        ]
    }
    return render(request, 'domingos/09/karaoke.html', context)

@login_required
def domingo10_karaoke(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')

    seccion_titulo = 'Conversión'
    puntos_totales = 0
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 10, 'karaoke')
        puntos_totales = obtener_puntos_totales_nino(nino)
        seccion = Section.objects.get(id=10)
        seccion_titulo = seccion.titulo
    except:
        pass

    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Karaoke",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Karaoke", 'url': None},
        ]
    }
    return render(request, 'domingos/10/karaoke.html', context)

@login_required
def domingo11_karaoke(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')

    seccion_titulo = 'Candelaria'
    puntos_totales = 0
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 11, 'karaoke')
        puntos_totales = obtener_puntos_totales_nino(nino)
        seccion = Section.objects.get(id=11)
        seccion_titulo = seccion.titulo
    except:
        pass

    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Karaoke",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Karaoke", 'url': None},
        ]
    }
    return render(request, 'domingos/11/karaoke.html', context)

@login_required
def domingo12_karaoke(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')

    seccion_titulo = 'Confianza'
    puntos_totales = 0
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 12, 'karaoke')
        puntos_totales = obtener_puntos_totales_nino(nino)
        seccion = Section.objects.get(id=12)
        seccion_titulo = seccion.titulo
    except:
        pass

    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Karaoke",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Karaoke", 'url': None},
        ]
    }
    return render(request, 'domingos/12/karaoke.html', context)

@login_required
def domingo13_karaoke(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')

    seccion_titulo = 'Navdad'
    puntos_totales = 0
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 13, 'karaoke')
        puntos_totales = obtener_puntos_totales_nino(nino)
        seccion = Section.objects.get(id=13)
        seccion_titulo = seccion.titulo
    except:
        pass

    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Karaoke",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Karaoke", 'url': None},
        ]
    }
    return render(request, 'domingos/13/karaoke.html', context)

@login_required
def domingo14_karaoke(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')

    seccion_titulo = 'Navdad'
    puntos_totales = 0
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 14, 'karaoke')
        puntos_totales = obtener_puntos_totales_nino(nino)
        seccion = Section.objects.get(id=14)
        seccion_titulo = seccion.titulo
    except:
        pass

    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Karaoke",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Karaoke", 'url': None},
        ]
    }
    return render(request, 'domingos/14/karaoke.html', context)

@login_required
def domingo15_karaoke(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')

    seccion_titulo = 'Navdad'
    puntos_totales = 0
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, 15, 'karaoke')
        puntos_totales = obtener_puntos_totales_nino(nino)
        seccion = Section.objects.get(id=15)
        seccion_titulo = seccion.titulo
    except:
        pass

    context = {
        'nino_nombre': nino_nombre,
        'puntos_totales': puntos_totales,
        'seccion_titulo': seccion_titulo,
        'breadcrumb_title': f"{seccion_titulo} - Karaoke",
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': f"{seccion_titulo} - Karaoke", 'url': None},
        ]
    }
    return render(request, 'domingos/15/karaoke.html', context)

@login_required
def select_nino(request):
    """Vista para seleccionar qué niño accede"""
    ninos = UsuarioNino.objects.filter(user=request.user)
    
    if not ninos.exists():
        messages.warning(request, 'Necesitas agregar al menos un niño en el Dashboard Premium.')
        return redirect('premium-dashboard')
    
    if request.method == 'POST':
        nino_id = request.POST.get('nino_id')
        if nino_id:
            nino = ninos.filter(id=nino_id).first()
            if nino:
                request.session['nino_id'] = nino.id
                request.session['nino_nombre'] = nino.nombre
                next_url = request.GET.get('next', 'dashboard')
                return redirect(next_url)
    
    # Si solo hay un niño, seleccionarlo automáticamente
    if ninos.count() == 1:
        nino = ninos.first()
        request.session['nino_id'] = nino.id
        request.session['nino_nombre'] = nino.nombre
        next_url = request.GET.get('next', 'dashboard')
        return redirect(next_url)
    
    next_url = request.GET.get('next', '')
    return render(request, 'select_nino.html', {'ninos': ninos, 'next_url': next_url})

def _render_domingo_index(request, numero_domingo):
    """Vista base para domingo/1 ... domingo/52 renderizando domingo/NN/index4.html."""
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")

    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    tareas_progreso = []
    puntos_totales = 0
    seccion_titulo = f"Domingo {numero_domingo}"

    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        seccion = Section.objects.filter(numero=numero_domingo).order_by('id').first()
        if not seccion:
            seccion = Section.objects.get(id=numero_domingo)
        seccion_titulo = seccion.titulo
        tareas = seccion.tareas.all().order_by('numero')

        for tarea in tareas:
            tarea_nino = TareaNino.objects.filter(nino=nino, tarea=tarea).first()
            tareas_progreso.append({
                'tarea': tarea,
                'completada': tarea_nino.completada if tarea_nino else False,
                'fecha_completado': tarea_nino.fecha_completado if tarea_nino else None,
            })

        puntos_totales = obtener_puntos_totales_nino(nino)
    except Exception:
        pass

    context = {
        'nino_nombre': nino_nombre,
        'seccion_titulo': seccion_titulo,
        'tareas_progreso': tareas_progreso,
        'puntos_totales': puntos_totales,
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': seccion_titulo, 'url': None},
        ]
    }

    return render(request, f'domingo/{numero_domingo:02d}/index4.html', context)


@login_required
def domingo1(request):
    return _render_domingo_index(request, 1)


@login_required
def domingo2(request):
    return _render_domingo_index(request, 2)


@login_required
def domingo3(request):
    return _render_domingo_index(request, 3)


@login_required
def domingo4(request):
    return _render_domingo_index(request, 4)


def _build_domingo_view(numero_domingo):
    @login_required
    def _view(request):
        return _render_domingo_index(request, numero_domingo)

    _view.__name__ = f"domingo{numero_domingo}"
    return _view


for _numero_domingo in range(5, 53):
    globals()[f"domingo{_numero_domingo}"] = _build_domingo_view(_numero_domingo)


def ensure_roles():
    for name in ['usuario', 'premium', 'admin']:
        Group.objects.get_or_create(name=name)


# Registro
def register_view(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			ensure_roles()
			user = form.save()
			group = Group.objects.get(name='usuario')
			user.groups.add(group)
			login(request, user)
			return redirect('home')
	else:
		form = RegisterForm()
	return render(request, 'register.html', {'form': form})

# Login
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout
def logout_view(request):
	logout(request)
	return redirect('landing')

# Home protegida
def home(request):
	return render(request, 'home.html')

# @login_required
def dashboard(request):
    has_premium = False
    nino_nombre = None
    nino_id = None
    
    # Obtener todas las secciones (hasta 52)
    secciones = Section.objects.all().order_by('numero')[:52]
    
    if request.user.is_authenticated:
        has_premium = user_has_premium_access(request.user)
        nino_nombre = request.session.get('nino_nombre')
        nino_id = request.session.get('nino_id')
    
    context = {
        'secciones': secciones,
        'has_premium': has_premium,
        'nino_nombre': nino_nombre,
        'nino_id': nino_id
    }
    return render(request, 'dashboard.html', context)


def user_has_premium_access(user):
    return user.is_superuser or user.groups.filter(name__in=['premium', 'admin']).exists()


@login_required
def premium_dashboard(request):
    ensure_roles()
    if not user_has_premium_access(request.user):
        messages.error(request, 'No tienes acceso premium.')
        return redirect('dashboard')

    ninos = UsuarioNino.objects.filter(user=request.user).order_by('nombre')
    if request.method == 'POST':
        form = UsuarioNinoForm(request.POST)
        if form.is_valid():
            nino = form.save(commit=False)
            nino.user = request.user
            nino.save()
            messages.success(request, f'✅ {nino.nombre} ha sido agregado exitosamente.')
            return redirect('premium-dashboard')
    else:
        form = UsuarioNinoForm()

    return render(request, 'premium_dashboard.html', {'form': form, 'ninos': ninos})


@login_required
def seccion_tareas(request, seccion_id):
    """Vista para mostrar las tareas de una sección y el progreso del niño"""
    # Verificar si hay un niño seleccionado
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Obtener el niño y la sección
    nino = get_object_or_404(UsuarioNino, id=nino_id, user=request.user)
    seccion = get_object_or_404(Section, id=seccion_id)
    
    # Obtener todas las tareas de la sección
    tareas = seccion.tareas.all().order_by('numero')
    
    # Obtener el progreso del niño para cada tarea
    tareas_progreso = []
    for tarea in tareas:
        tarea_nino = TareaNino.objects.filter(nino=nino, tarea=tarea).first()
        tareas_progreso.append({
            'tarea': tarea,
            'completada': tarea_nino.completada if tarea_nino else False,
            'fecha_completado': tarea_nino.fecha_completado if tarea_nino else None,
            'tarea_nino_id': tarea_nino.id if tarea_nino else None
        })
    
    # Calcular estadísticas
    total_tareas = len(tareas)
    tareas_completadas = sum(1 for t in tareas_progreso if t['completada'])
    porcentaje = (tareas_completadas / total_tareas * 100) if total_tareas > 0 else 0
    
    context = {
        'seccion': seccion,
        'tareas_progreso': tareas_progreso,
        'nino': nino,
        'nino_nombre': nino_nombre,
        'total_tareas': total_tareas,
        'tareas_completadas': tareas_completadas,
        'porcentaje': round(porcentaje, 1)
    }
    
    return render(request, 'tareas/seccion_tareas.html', context)


@login_required
@require_POST
def toggle_tarea(request, tarea_id):
    """Marca una tarea como completada o no completada para un niño"""
    # Verificar si hay un niño seleccionado
    if 'nino_id' not in request.session:
        return JsonResponse({'error': 'No hay niño seleccionado'}, status=400)

    try:
        nino_id = request.session.get('nino_id')
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        tarea = Tarea.objects.get(id=tarea_id)

        # Obtener o crear TareaNino asegurando el usuario requerido
        tarea_nino, created = TareaNino.objects.get_or_create(
            nino=nino,
            tarea=tarea,
            defaults={'usuario': request.user}
        )

        # Toggle completada
        tarea_nino.completada = not tarea_nino.completada
        tarea_nino.fecha_completado = timezone.now() if tarea_nino.completada else None
        tarea_nino.save()

        # Si todas las tareas de la sección están completadas, marcar sección como completada
        seccion = tarea.seccion
        tareas_seccion = seccion.tareas.all()
        todas_completas = all(
            TareaNino.objects.filter(nino=nino, tarea=t, completada=True).exists()
            for t in tareas_seccion
        )

        if todas_completas:
            registrar_actividad_completada(nino, seccion.id, 'tareas')

        return JsonResponse({
            'success': True,
            'completada': tarea_nino.completada,
            'fecha_completado': tarea_nino.fecha_completado.strftime('%d/%m/%Y %H:%M') if tarea_nino.fecha_completado else None
        })
    except UsuarioNino.DoesNotExist:
        return JsonResponse({'error': 'Niño no encontrado'}, status=404)
    except Tarea.DoesNotExist:
        return JsonResponse({'error': 'Tarea no encontrada'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@login_required
@require_POST
def registrar_actividad(request, seccion_id, actividad):
	"""Registra que un niño completó una actividad en una sección"""
	if 'nino_id' not in request.session:
		return JsonResponse({'error': 'No hay niño seleccionado'}, status=400)
	
	try:
		nino_id = request.session.get('nino_id')
		nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
		
		resultado = registrar_actividad_completada(nino, seccion_id, actividad)
		
		if 'error' in resultado:
			return JsonResponse(resultado, status=400)
		
		return JsonResponse({
			'success': True,
			'puntos_totales': resultado['puntos_totales'],
			'mensaje': resultado['mensaje'],
			'nueva_actividad': resultado.get('nueva_actividad', False)
		})
	except UsuarioNino.DoesNotExist:
		return JsonResponse({'error': 'Niño no encontrado'}, status=404)
	except Exception as e:
		return JsonResponse({'error': str(e)}, status=500)


# @login_required
# @require_POST
# def toggle_tarea(request, tarea_id):
#     """Vista AJAX para marcar/desmarcar una tarea como completada"""
#     # Verificar si hay un niño seleccionado
#     if 'nino_id' not in request.session:
#         return JsonResponse({'success': False, 'error': 'No hay niño seleccionado'})
    
#     nino_id = request.session.get('nino_id')
    
#     try:
#         # Obtener el niño y la tarea
#         nino = get_object_or_404(UsuarioNino, id=nino_id, user=request.user)
#         tarea = get_object_or_404(Tarea, id=tarea_id)
        
#         # Obtener o crear el registro de TareaNino
#         tarea_nino, created = TareaNino.objects.get_or_create(
#             usuario=request.user,
#             nino=nino,
#             tarea=tarea
#         )
        
#         # Toggle: cambiar el estado de completada
#         tarea_nino.completada = not tarea_nino.completada
        
#         # Si se marca como completada, guardar fecha y hora
#         if tarea_nino.completada:
#             tarea_nino.fecha_completado = timezone.now()
#         else:
#             tarea_nino.fecha_completado = None
        
#         tarea_nino.save()
        
#         return JsonResponse({
#             'success': True,
#             'completada': tarea_nino.completada,
#             'fecha_completado': tarea_nino.fecha_completado.strftime('%d/%m/%Y %H:%M') if tarea_nino.fecha_completado else None
#         })
    
#     except Exception as e:
#         return JsonResponse({'success': False, 'error': str(e)})

