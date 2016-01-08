from django.shortcuts import render, redirect
from app.forms import ClassARegistrationForm, ClassBRegistrationForm
from app.models import ClassA, ClassB

def addpassengerA(request):
	capacity = 10
	form = ClassARegistrationForm()
	if request.method == 'POST':
		form = ClassARegistrationForm()
		if form.is_valid() and capacity>0:
			capacity-=1
			form.save()
			return redirect('success')
		else:
			return redirect('full')
	return render(request, 'addpassengerA.html', {'form': form})

def addpassengerB(request):
	capacity = 10
	form = ClassBRegistrationForm
	if request.method == 'POST':
		form = ClassBRegistrationForm()
		if form.is_valid() and capacity>0:
			capacity-=1
			form.save()
			return redirect('success')
		else:
			return redirect('full')
	return render(request, 'addpassengerB.html', {'form': form})

def home(request):
	return render(request, 'home.html')

def success(request):
	return render(request, 'success.html')

def full(request):
	return render(request, 'full.html')



