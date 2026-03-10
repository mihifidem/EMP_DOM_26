$filePath = 'c:\Proyectos\EMP_DOM_\core\views.py'
$content = Get-Content -Path $filePath -Raw -Encoding UTF8

$functions = @()
for ($i = 16; $i -le 52; $i++) {
    $seccionId = $i - 1
    $func = @"

@login_required
def domingo${i}_infografia(request):
    if 'nino_id' not in request.session:
        return redirect(f"/select-nino/?next={request.path}")
    nino_id = request.session.get('nino_id')
    nino_nombre = request.session.get('nino_nombre', 'Niño')
    
    # Registrar actividad
    seccion_titulo = 'Navidad'
    try:
        nino = UsuarioNino.objects.get(id=nino_id, user=request.user)
        registrar_actividad_completada(nino, ${seccionId}, 'infografia')
        seccion = Section.objects.get(id=${seccionId})
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
    return render(request, 'domingos/${i}/infografia.html', context)
"@
    $functions += $func
}

$insertBlock = ($functions -join "")
$marker = "return render(request, 'domingos/15/infografia.html', context)"
$index = $content.IndexOf($marker)

if ($index -lt 0) {
    Write-Error 'No se encontro la funcion domingo15_infografia.'
    exit 1
}

$afterMarker = $index + $marker.Length
$newContent = $content.Insert($afterMarker, $insertBlock)
Set-Content -Path $filePath -Value $newContent -Encoding UTF8
Write-Host 'Funciones insertadas correctamente.'
