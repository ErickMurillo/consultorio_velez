from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import *

# Create your views here.
def index(request,template="index.html"):
	casos = Casos.objects.all().order_by('-id')[:3]

	if request.method == 'POST':
		mensaje = None
		form = EmailForm(request.POST)
		if form.is_valid():
			request.session['name'] = form.cleaned_data['name']
			request.session['email'] = form.cleaned_data['email']
			request.session['phone'] = form.cleaned_data['phone']
			request.session['message'] = form.cleaned_data['message']
			
			mensaje = "Todas las variables estan correctamente :)"
			request.session['activo'] = True
			centinela = 1

			return HttpResponseRedirect('/')

		else:
			centinela = 0

	else:
		form = EmailForm()
		mensaje = "Existen alguno errores"
		centinela = 0
		try:
			del request.session['name']
			del request.session['email']
			del request.session['phone']
			del request.session['message']
		except:
			pass
	return render(request, template, locals())


def detalle(request, slug, template="detail.html"):
	caso = Casos.objects.get(slug=slug)
	return render(request, template, locals())

# def send_mail(request):
# 	if request.method == 'POST':
# 		form = EmailForm(request.POST)
# 		if form.is_valid():
# 			name = form.cleaned_data['name']
# 			email = form.cleaned_data['email']
# 			phone = form.cleaned_data['phone']
# 			message = form.cleaned_data['message']
# 			if botcheck == 'yes':
# 				try:
# 					fullemail = firstname + " " + lastname + " " + "<" + email + ">"
# 					send_mail(subject, message, fullemail, ['SENDTOUSER@DOMAIN.COM'])
# 					return HttpResponseRedirect('/email/thankyou/')
# 				except:
# 					return HttpResponseRedirect('/email/')
# 		else:
# 			return HttpResponseRedirect('/email/')
# 	else:
# 		return HttpResponseRedirect('/email/')  
		
# 	return render(request, template, locals())