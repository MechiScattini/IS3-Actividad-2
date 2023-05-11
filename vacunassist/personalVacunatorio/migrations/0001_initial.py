# Generated by Django 4.0.3 on 2022-07-06 20:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pacientes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuariosAdministradores',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Administradores de Vacunatorios',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('pacientes.usuarios',),
        ),
        migrations.CreateModel(
            name='PersonalDetalles',
            fields=[
                ('personal_id', models.AutoField(primary_key=True, serialize=False)),
                (
                    'nombre',
                    models.CharField(default='m', max_length=100, verbose_name='Nombre')
                ),
                (
                    'apellido',
                    models.CharField(default='m', max_length=100, verbose_name='Apellido')
                ),
                (
                    'numero_telefono',
                    models.CharField(max_length=20, verbose_name='Número Teléfono')
                ),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de Nacimiento')),
                (
                    'centro_vacunatorio',
                    models.CharField(max_length=50, verbose_name='Centro Vacunatorio')
                ),
                (
                    'user',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL
                    )
                ),
            ],
            options={
                'verbose_name': 'Detalles Personal',
                'db_table': 'personal_detalles',
            },
        ),
    ]
