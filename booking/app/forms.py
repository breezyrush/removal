from django import forms
from app.models import ClassA, ClassB

class ClassARegistrationForm(forms.ModelForm):
	class Meta:
		model = ClassA
		fields = ('passengerA',)

class ClassBRegistrationForm(forms.ModelForm):
	class Meta:
		model = ClassB
		fields = ('passengerB',)