from django.core.management.base import BaseCommand
from books.models import ColorCard


class Command(BaseCommand):
    help = 'Crea los colores de tarjeta incluyendo colores litúrgicos'

    def handle(self, *args, **options):
        colores_config = [
            {
                'nombre': 'azul',
                'display_name': 'Azul',
                'gradiente_css': 'linear-gradient(135deg, #48c6ef 0%, #6f86d6 100%)',
                'es_liturgico': False,
                'descripcion_liturgica': None,
            },
            {
                'nombre': 'violeta',
                'display_name': 'Violeta',
                'gradiente_css': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
                'es_liturgico': True,
                'descripcion_liturgica': 'Penitencia y conversión (Adviento, Cuaresma)',
            },
            {
                'nombre': 'verde',
                'display_name': 'Verde',
                'gradiente_css': 'linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%)',
                'es_liturgico': True,
                'descripcion_liturgica': 'Esperanza y vida eterna (Tiempo Ordinario)',
            },
            {
                'nombre': 'naranja',
                'display_name': 'Naranja',
                'gradiente_css': 'linear-gradient(135deg, #fa709a 0%, #fee140 100%)',
                'es_liturgico': False,
                'descripcion_liturgica': None,
            },
            {
                'nombre': 'rosa',
                'display_name': 'Rosa',
                'gradiente_css': 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
                'es_liturgico': False,
                'descripcion_liturgica': 'Variante del violeta para domingos especiales',
            },
            {
                'nombre': 'turquesa',
                'display_name': 'Turquesa',
                'gradiente_css': 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
                'es_liturgico': False,
                'descripcion_liturgica': None,
            },
            {
                'nombre': 'indigo',
                'display_name': 'Índigo',
                'gradiente_css': 'linear-gradient(135deg, #7f7fd5 0%, #86a8e7 100%)',
                'es_liturgico': False,
                'descripcion_liturgica': None,
            },
            {
                'nombre': 'rojo',
                'display_name': 'Rojo',
                'gradiente_css': 'linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%)',
                'es_liturgico': True,
                'descripcion_liturgica': 'Martirio y sangre de Cristo (Pasión, mártires)',
            },
            {
                'nombre': 'blanco',
                'display_name': 'Blanco',
                'gradiente_css': 'linear-gradient(135deg, #e0eafc 0%, #cfdef3 100%)',
                'es_liturgico': False,
                'descripcion_liturgica': 'Pureza y gozo (Navidad, Pascua, santos)',
            },
        ]

        for config in colores_config:
            color, created = ColorCard.objects.get_or_create(
                nombre=config['nombre'],
                defaults={
                    'display_name': config['display_name'],
                    'gradiente_css': config['gradiente_css'],
                    'es_liturgico': config['es_liturgico'],
                    'descripcion_liturgica': config['descripcion_liturgica'],
                }
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"✓ Color '{config['display_name']}' creado.")
                )
            else:
                self.stdout.write(f"  Color '{config['display_name']}' ya existe.")

        self.stdout.write(
            self.style.SUCCESS('\n✓ Colores litúrgicos configurados: Verde, Violeta, Rojo')
        )
