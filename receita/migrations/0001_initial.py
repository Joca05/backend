

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),

        
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('ingredientes', models.TextField()),
                ('modo_preparo', models.TextField()),
                ('imagem', models.ImageField(upload_to='receita/upload', null=True, blank=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='receita',
                    to=settings.AUTH_USER_MODEL
                )),
                ('categoria', models.ForeignKey(
                    on_delete=django.db.models.deletion.SET_NULL,
                    null=True,
                    related_name='receita',
                    to='receita.categoria'
                )),
            ],
        ),

        
        migrations.CreateModel(
            name='Interacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=3, choices=[('COM', 'Comentário'), ('AVA', 'Avaliação')])),
                ('comentario', models.TextField(null=True, blank=True)),
                ('estrelas', models.IntegerField(null=True, blank=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('receita', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='interacoes',
                    to='receita.receita'
                )),
                ('usuario', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL
                )),
            ],
        ),

        migrations.CreateModel(
            name='Visualizacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('receita', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='visualizacoes',
                    to='receita.receita'
                )),
            ],
        ),
    ]
