import json
from pathlib import Path

from django.core.management.base import BaseCommand
from django.conf import settings

from books.models import Section, Tarea, Book


class Command(BaseCommand):
    help = "Importa los 52 domingos y sus tareas desde domingos.json"

    def handle(self, *args, **kwargs):

        ruta_json = Path(settings.BASE_DIR) / "data" / "domingos.json"

        if not ruta_json.exists():
            self.stdout.write(self.style.ERROR("No se encontró domingos.json"))
            return

        with open(ruta_json, "r", encoding="utf-8") as f:
            domingos = json.load(f)

        # Usar libro existente
        try:
            libro = Book.objects.get(id=1)
        except Book.DoesNotExist:
            self.stdout.write(self.style.ERROR("No existe el libro con id=1"))
            return

        total_secciones = 0
        total_tareas = 0

        for d in domingos:

            seccion, created = Section.objects.update_or_create(
                libro=libro,
                numero=d["numero_domingo"],
                defaults={
                    "titulo": d["titulo"],
                    "contenido": d["descripcion"],
                    "fecha_inicio": d["fecha_inicio"],
                    "fecha_fin": d["fecha_fin"],
                }
            )

            total_secciones += 1

            for i, tarea_texto in enumerate(d["tareas"], start=1):

                Tarea.objects.update_or_create(
                seccion=seccion,
                numero=i,
                defaults={
                    "titulo": tarea_texto,
                    "descripcion": tarea_texto,
                    "tipo": "ejercicio"
                    }
                )

                total_tareas += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"✔ Importadas {total_secciones} secciones y {total_tareas} tareas correctamente"
            )
        )