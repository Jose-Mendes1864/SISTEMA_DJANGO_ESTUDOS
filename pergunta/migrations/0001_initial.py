# Generated by Django 5.0.2 on 2024-03-02 15:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pergunta.area')),
            ],
        ),
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enuciado', models.CharField(max_length=505)),
                ('resposta', models.CharField(max_length=200)),
                ('assunto', models.CharField(max_length=200)),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pergunta.materia')),
            ],
        ),
        migrations.CreateModel(
            name='Pergunta_simulado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respondido', models.BooleanField(default=False)),
                ('acertou', models.BooleanField(default=False)),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pergunta.pergunta')),
            ],
        ),
        migrations.CreateModel(
            name='Simulado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('quantidade', models.IntegerField()),
                ('feito', models.IntegerField(default=0)),
                ('area_pertence', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pergunta.area')),
                ('materia', models.ForeignKey(default='todas', on_delete=django.db.models.deletion.DO_NOTHING, to='pergunta.materia')),
            ],
        ),
    ]
