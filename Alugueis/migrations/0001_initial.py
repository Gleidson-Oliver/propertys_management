# Generated by Django 5.0.1 on 2024-01-30 01:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Casa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, default='', upload_to='alugueis/covers/%Y/%m/%d/')),
                ('cidade', models.CharField(max_length=255)),
                ('rua', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=255)),
                ('disponivel', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inquilino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=15, unique=True)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('carne', models.FileField(upload_to='alugueis/covers/%Y/%m/%d/')),
                ('contrato', models.FileField(upload_to='alugueis/covers/%Y/%m/%d/')),
                ('Aluguel', models.CharField(default=None, max_length=255)),
                ('data_vencimento', models.DateField(unique=True)),
                ('casa', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Alugueis.casa')),
            ],
        ),
    ]