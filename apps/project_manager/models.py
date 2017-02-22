# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models

# Create your models here.
STATES = (('new', 'Nuevo'),	('process', 'En proceso'),	('validating', 'Validando'), ('rejected', 'Rechazado'), ('completed', 'Completado'),)

class Plan(models.Model):
	name = models.CharField(max_length=200, unique=True)
	sumary = models.TextField(max_length=255, default='')
	organizer = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)

	def __unicode__(self):
		return self.name

class Task(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
	plan = models.ForeignKey(Plan, null=True)
	labor = models.TextField(max_length=255, default='')
	content = models.TextField(max_length=255, default='')
	status = models.CharField(max_length=50, choices=STATES, null=True)

	def __unicode__(self):
		return self.labor

class Competitor(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
	plan = models.ManyToManyField(Plan, null=True)