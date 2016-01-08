from __future__ import unicode_literals

from django.db import models

class ClassA(models.Model):
	passengerA = models.CharField(max_length = 120)

	def __unicode__(self):
		self.passengerA

class ClassB(models.Model):
	passengerB = models.CharField(max_length =120)

	def __unicode__(self):
		self.passengerB

