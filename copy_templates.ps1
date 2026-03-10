$sourceFolder = 'c:\Proyectos\EMP_DOM_\core\templates\domingos\15'
$files = Get-ChildItem -Path $sourceFolder -File

for ($i = 16; $i -le 52; $i++) {
    $destFolder = "c:\Proyectos\EMP_DOM_\core\templates\domingos\$i"
    
    if (!(Test-Path $destFolder)) {
        New-Item -ItemType Directory -Path $destFolder -Force | Out-Null
    }
    
    foreach ($file in $files) {
        $destFile = Join-Path $destFolder $file.Name
        Copy-Item -Path $file.FullName -Destination $destFile -Force
    }
    
    Write-Host "Copiados archivos a: domingos\$i"
}
Write-Host 'Completado!'
