$content = Get-Content 'c:\Proyectos\EMP_DOM_\core\templates\domingo\17\index4.html' -Raw

for ($i = 18; $i -le 52; $i++) {
    $folder = "c:\Proyectos\EMP_DOM_\core\templates\domingo\$i"
    New-Item -ItemType Directory -Path $folder -Force | Out-Null
    $newContent = $content -replace '17', $i.ToString()
    Set-Content -Path "$folder\index4.html" -Value $newContent -Encoding UTF8
    Write-Host "Creado: $folder\index4.html"
}
