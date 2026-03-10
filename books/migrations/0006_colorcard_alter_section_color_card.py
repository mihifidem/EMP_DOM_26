# Generated migration for ColorCard model

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_section_color_card'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(choices=[('azul', 'Azul'), ('violeta', 'Violeta'), ('verde', 'Verde'), ('naranja', 'Naranja'), ('rosa', 'Rosa'), ('turquesa', 'Turquesa'), ('indigo', 'Índigo'), ('rojo', 'Rojo'), ('blanco', 'Blanco')], max_length=20, unique=True)),
                ('display_name', models.CharField(max_length=50)),
                ('gradiente_css', models.CharField(help_text='Gradiente CSS del color', max_length=200)),
                ('es_liturgico', models.BooleanField(default=False, help_text='Indica si es un color litúrgico')),
                ('descripcion_liturgica', models.CharField(blank=True, help_text='Significado litúrgico del color', max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Color de Tarjeta',
                'verbose_name_plural': 'Colores de Tarjeta',
                'ordering': ['nombre'],
            },
        ),
        migrations.RemoveField(
            model_name='section',
            name='color_card',
        ),
        migrations.AddField(
            model_name='section',
            name='color_card',
            field=models.ForeignKey(default=None, help_text='Color del gradiente de la tarjeta', null=True, on_delete=models.deletion.SET_NULL, related_name='secciones', to='books.colorcard'),
        ),
    ]
