# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 12:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('sumary', models.TextField(default='', max_length=255)),
                ('organizer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='content',
            field=models.TextField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='task',
            name='labor',
            field=models.TextField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('new', 'Nuevo'), ('process', 'En proceso'), ('validating', 'Validando'), ('rejected', 'Rechazado'), ('completed', 'Completado')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='competitor',
            name='plan',
            field=models.ManyToManyField(null=True, to='project_manager.Plan'),
        ),
        migrations.AddField(
            model_name='competitor',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='task',
            name='plan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_manager.Plan'),
        ),
    ]