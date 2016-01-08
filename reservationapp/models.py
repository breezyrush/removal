from django.db import models

from django.contrib import admin

from schedule.models import Occurrence

from __future__ import unicode_literals

class SeatReservations(models.Model):
    occurrence = models.OneToOneField(Occurrence)
    reservation_limit = models.IntegerField(default=10) 
    reservations = models.ManyToManyField(User, blank=True)


   
    def reserved(self,):
        
        count = self.reservations.filter.count()
        if count > 0:
            return True
        else:
            return False

    def has_limit(self):
        return self.reservation_limit != 0

    def can_rsvp(self):
       
        if self.reservation_limit <= 0:
            return True

        count = self.reservations.count()
        if count >= self.reservation_limit:
            return False

        return True

class classA(models.Model):
    passengerA = models.CharField(max_length=120)

    def __unicode__(self):
        self.passengerA

class classB(models.Model):
    passengerB = models.CharField(max_length=120)

    def __unicode__(self):
        self.passengerB
