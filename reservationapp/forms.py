from django import forms

from reservationapp.models import SeatReservations

class RsvpForm(forms.ModelForm):
    reserved = forms.BooleanField(initial=True, required=False)

    def clean(self):
        data = self.cleaned_data

        if data['attending']:
            try:
                er = self.instance.seatreservations
            except SeatReservations.DoesNotExist:
                er = SeatReservations(occurrence=self.instance)
                er.save()

                if not er.can_rsvp():
                    raise forms.ValidationError("Seat is already taken.")
        return data

    class Meta:
        model = Occurrence
        exclude = ('passenger')