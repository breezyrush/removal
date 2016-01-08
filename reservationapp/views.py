from django.shortcuts import render

# Create your views here.

def reservations(request, occurrence_id,
                         template_name='reservationapp/reservation.html'):
    
    occurrence = get_object_or_404(Occurrence, pk=occurrence_id)
    try:
        er = occurrence.eventreservations
    except SeatReservations.DoesNotExist:
        er = SeatReservations(occurrence=occurrence)
        er.save()

    rsvpers = er.reservations.all().order_by('passenger_name')

    context = RequestContext(request, {'occurrence': occurrence,er': er,rsvpers': rsvpers})

    return render_to_response(template_name, context)



def rsvp(request, occurrence_id, template_name='reservationapp/rsvp.html'):
    
    
    occurrence = get_object_or_404(Occurrence, pk=occurrence_id)

    try:
        er = occurrence.seatreservations
        reserved = er.post_reserved(request.POST)
    except SeatReservations.DoesNotExist:
        reserved = False

    if request.method == "POST":
        form = RsvpForm(data=request.POST, instance=occurrence)
        if form.is_valid():
            occurrence = form.save()
            if form.cleaned_data['reserved']:
                occurrence.eventreservations.reservations.add(request.POST)
            else:
                try:
                    er = occurrence.eventreservations
                    er.reservations.remove(request.POST)
                except SeatReservations.DoesNotExist:
                    pass # no reservations exist

            return HttpResponseRedirect(reverse('reservations_reservations_view', kwargs={'occurrence_id':occurrence.pk}))
    else:
        form = RsvpForm(initial={'reserved':reserved}, instance=occurrence)



    context = RequestContext(request, {'form':form, 'occurrence':occurrence, 'reserved':reserved})

    return render_to_response(template_name, context)

