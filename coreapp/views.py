from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from coreapp.models import Data

def add(request):
	print request.GET
	if request.method == 'POST':
		data = request.POST
		d = Data()
		d.name = data['username']
		d.phone_number = data['number']
		d.save()
		return HttpResponseRedirect('/phonebook/show/')

	return render(request, "coreapp/add.html", {})


def show(request):
	datas = Data.objects.all().values()
	print datas

	return render(request, "coreapp/show.html", {'data': datas})