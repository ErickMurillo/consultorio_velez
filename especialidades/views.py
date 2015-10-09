from django.shortcuts import render
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

# Create your views here.
def index(request,template="index.html"):
	casos = Casos.objects.all().order_by('-id')[:6]
	info = Informacion.objects.all()[:1].get()
	experiencia = Experiencia.objects.all()[:1].get()

	return render(request, template, locals())

def lista_casos(request, template="casos_list.html"):
	casos = Casos.objects.all().order_by('-id')

	return render(request, template, locals())

def detalle(request, slug, template="detail.html"):
	caso = Casos.objects.get(slug=slug)
	return render(request, template, locals())

def ortopedia(request, template="casos_list.html"):
	casos = Casos.objects.filter(categoria=1).order_by('-id')

	return render(request, template, locals())

def trauma(request, template="casos_list.html"):
	casos = Casos.objects.filter(categoria=2).order_by('-id')
	
	return render(request, template, locals())

def artroscopia(request, template="casos_list.html"):
	casos = Casos.objects.filter(categoria=3).order_by('-id')
	
	return render(request, template, locals())

def cirugia_biologica(request, template="casos_list.html"):
	casos = Casos.objects.filter(categoria=4).order_by('-id')
	
	return render(request, template, locals())

def contacto(request, template="contacto.html"):
	arreglo_mail = ['erickmurillo22@gmail.com']

	if request.method == 'POST':
		form = EmailForm(request.POST)
		print form
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			phone = form.cleaned_data['phone']
			message = form.cleaned_data['message']
			try:
				subject, from_email, to = 'Una persona desea contactarlo en la web Dr. Velez Ponce', 'noreply@drvelezponce.com', arreglo_mail
				text_content = "Una persona desea contactarlo en la web Dr. Velez Ponce " + \
								'Nombre: ' + name + ', '  + \
								'Telefono: ' + phone + ', ' + \
								'Email: ' + email + ', ' + \
								'Mensaje: '+ \
								 message
				html_content = "Una persona desea contactarlo en la web Dr. Velez Ponce " + \
								'Nombre: ' + name + ', '  + \
								'Telefono: ' + phone + ', ' + \
								'Email: ' + email + ', ' + \
								'Mensaje: '+ \
								 message 
				msg = EmailMultiAlternatives(subject, text_content, from_email, arreglo_mail)
				msg.attach_alternative(html_content, "text/html")
				msg.send()

				return HttpResponseRedirect('/')
			except:
				pass
			
	else:
		form = EmailForm()
	return render(request, template, locals())

def send_mail():
	pass

