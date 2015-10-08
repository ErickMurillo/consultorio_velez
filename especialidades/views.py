from django.shortcuts import render
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request,template="index.html"):
	casos = Casos.objects.all().order_by('-id')[:3]
	# if request.method == 'POST':
	# 	form = EmailForm(request.POST)
	# 	if form.is_valid():
	# 		name = form.cleaned_data['name']
	# 		email = form.cleaned_data['email']
	# 		phone = form.cleaned_data['phone']
	# 		message = form.cleaned_data['message']
	# 		subject = 'prueba'
	# 		#send_mail(subject, message, 'erickmurillo22@gmail.com',['erickmurillo22@gmail.com'], fail_silently=False)
			
	# 		return HttpResponseRedirect('/')
	# else:
	# 	form = EmailForm()
	return render(request, template, locals())


def detalle(request, slug, template="detail.html"):
	caso = Casos.objects.get(slug=slug)
	return render(request, template, locals())

