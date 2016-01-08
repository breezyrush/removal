from django.conf.urls.defaults import *

urlpatterns = patterns('reservationapp.views'),

url(r'^(?P<occurrence_id>\d+)/$', 'reservations',  name="reservations_reservations_view"),

url(r'^(?P<occurrence_id>\d+)/rsvp/$', 'rsvp', name="reservations_rsvp"),