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
	casos = Casos.objects.all().order_by('-id')[:6]

	if request.method == 'POST':
		mensaje = None
		form = EmailForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data.get('name')
			#email = form.cleaned_data.get['email']
			#phone = form.cleaned_data.get('phone')
			#message = form.cleaned_data.get('message')
			
			subject = 'Prueba'
			from_email = settings.EMAIL_HOST_USER
			to_email = 'erick_murillo92@hotmail.com'
			contact_message = "%s" %(name)
			try:
				send_mail(subject, contact_message, from_email, to_email, fail_silently=False)
				return HttpResponseRedirect('/')
			except:
				pass

	else:
		form = EmailForm()

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