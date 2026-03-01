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
    return render(request, 'domingos/01/karaoke.html', context)


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

@login_required
def domingo4(request):
    # Verificar si hay un niño seleccionado
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Obtener el niño y las tareas de la sección 4 (IV Domingo de Adviento)
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        seccion = Section.objects.get(id=4)
        tareas = seccion.tareas.all().order_by('numero')
        
        # Obtener el progreso del niño para cada tarea
        tareas_progreso = []
        for tarea in tareas:
            tarea_nino = TareaNino.objects.filter(nino=nino, tarea=tarea).first()
            tareas_progreso.append({
                'tarea': tarea,
                'completada': tarea_nino.completada if tarea_nino else False,
                'fecha_completado': tarea_nino.fecha_completado if tarea_nino else None,
            })
        
        # Obtener los puntos totales del niño
        puntos_totales = obtener_puntos_totales_nino(nino)
    except:
        tareas_progreso = []
        puntos_totales = 0
    
    context = {
        'nino_nombre': nino_nombre,
        'tareas_progreso': tareas_progreso,
        'puntos_totales': puntos_totales,
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': 'IV Domingo de Adviento', 'url': None},
        ]
    }
    
    return render(request, 'domingo/04/index4.html', context) 

@login_required
def domingo3(request):
    # Verificar si hay un niño seleccionado
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Obtener el niño y las tareas de la sección 3 (III Domingo de Adviento)
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        seccion = Section.objects.get(id=3)
        tareas = seccion.tareas.all().order_by('numero')
        
        # Obtener el progreso del niño para cada tarea
        tareas_progreso = []
        for tarea in tareas:
            tarea_nino = TareaNino.objects.filter(nino=nino, tarea=tarea).first()
            tareas_progreso.append({
                'tarea': tarea,
                'completada': tarea_nino.completada if tarea_nino else False,
                'fecha_completado': tarea_nino.fecha_completado if tarea_nino else None,
            })
        
        # Obtener los puntos totales del niño
        puntos_totales = obtener_puntos_totales_nino(nino)
    except:
        tareas_progreso = []
        puntos_totales = 0
    
    context = {
        'nino_nombre': nino_nombre,
        'tareas_progreso': tareas_progreso,
        'puntos_totales': puntos_totales,
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': 'III Domingo de Adviento', 'url': None},
        ]
    }
    
    return render(request, 'domingo/03/index4.html', context) 


@login_required
def domingo2(request):
    # Verificar si hay un niño seleccionado
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Obtener el niño y las tareas de la sección 2 (II Domingo de Adviento)
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        seccion = Section.objects.get(id=2)
        tareas = seccion.tareas.all().order_by('numero')
        
        # Obtener el progreso del niño para cada tarea
        tareas_progreso = []
        for tarea in tareas:
            tarea_nino = TareaNino.objects.filter(nino=nino, tarea=tarea).first()
            tareas_progreso.append({
                'tarea': tarea,
                'completada': tarea_nino.completada if tarea_nino else False,
                'fecha_completado': tarea_nino.fecha_completado if tarea_nino else None,
            })
        
        # Obtener los puntos totales del niño
        puntos_totales = obtener_puntos_totales_nino(nino)
    except:
        tareas_progreso = []
        puntos_totales = 0
    
    context = {
        'nino_nombre': nino_nombre,
        'tareas_progreso': tareas_progreso,
        'puntos_totales': puntos_totales,
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': 'II Domingo de Adviento', 'url': None},
        ]
    }
    
    return render(request, 'domingo/02/index4.html', context) 

@login_required
def domingo1(request):
    # Verificar si hay un niño seleccionado
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Obtener el niño y las tareas de la sección 1 (I Domingo de Adviento)
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        seccion = Section.objects.get(id=1)
        tareas = seccion.tareas.all().order_by('numero')
        
        # Obtener el progreso del niño para cada tarea
        tareas_progreso = []
        for tarea in tareas:
            tarea_nino = TareaNino.objects.filter(nino=nino, tarea=tarea).first()
            tareas_progreso.append({
                'tarea': tarea,
                'completada': tarea_nino.completada if tarea_nino else False,
                'fecha_completado': tarea_nino.fecha_completado if tarea_nino else None,
            })
        
        # Obtener los puntos totales del niño
        puntos_totales = obtener_puntos_totales_nino(nino)
    except:
        tareas_progreso = []
        puntos_totales = 0
    
    context = {
        'nino_nombre': nino_nombre,
        'tareas_progreso': tareas_progreso,
        'puntos_totales': puntos_totales,
        'breadcrumb_items': [
            {'label': 'Home', 'url': '/'},
            {'label': 'Los 52 Domingos', 'url': '/dashboard/'},
            {'label': 'I Domingo de Adviento', 'url': None},
        ]
    }
    
    return render(request, 'domingo/01/index4.html', context) 


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
		
		# Obtener o crear TareaNino
		tarea_nino, created = TareaNino.objects.get_or_create(nino=nino, tarea=tarea)
		
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
