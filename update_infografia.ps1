$templatePath = 'c:\Proyectos\EMP_DOM_\core\templates\domingos'

for ($i = 16; $i -le 52; $i++) {
    $filePath = "$templatePath\$i\infografia.html"
    
    if (Test-Path $filePath) {
        $content = Get-Content -Path $filePath -Raw -Encoding UTF8
        
        # Reemplazar /15 por el número actual en todas las URLs
        $newContent = $content -replace '/15/', "/$i/"
        $newContent = $newContent -replace 'DOM15', "DOM$('{0:D2}' -f $i)"
        
        Set-Content -Path $filePath -Value $newContent -Encoding UTF8
        Write-Host "Actualizado: domingos\$i\infografia.html"
    }
}
Write-Host 'Completado!'
