from django.shortcuts import render, redirect
from .models import CarsGM
from .forms import CarsForm

def homepage(request):

	queryset = CarsGM.objects.all()

	context = {'cars': queryset}

	return render(request, 'app1/homepage.html', context)


def createCars(request):
	form = CarsForm()

	if request.method=='POST':
		form = CarsForm(request.POST)
		if form.is_valid():
			form.save()

			return redirect('/')

	context = {'form':form}
	return render(request, 'app1/formCars.html', context)


def updateCars(request, pk):
	edit = CarsGM.objects.get(id=pk)
	form = CarsForm(instance=edit)

	if request.method=='POST':
		form = CarsForm(request.POST, instance=edit)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'app1/formCars.html', context)


def deleteCars(request, pk):

	form = CarsGM.objects.get(id=pk)
	if request.method=='POST':
		form.delete()

		return redirect('/')


	context = {'form':form}
	return render(request, 'app1/delete.html', context)