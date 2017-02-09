from django.shortcuts import render
from .models import *
from .forms import *
from expedientes.models import *
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.
class IndexView(TemplateView):
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['casos'] = Casos.objects.all().order_by('-id')[:6]
		context['info'] = Informacion.objects.all()[:1].get()
		context['experiencia'] = Experiencia.objects.all()[:1].get()
		return context

class ListCasosView(ListView):
	template_name = "casos_list.html"
	queryset = Casos.objects.all().order_by('-id')

class CasoDetail(DetailView):
	template_name = "detail.html"
	model = Casos

	def get_context_data(self, **kwargs):
		context = super(CasoDetail, self).get_context_data(**kwargs)
		context['casos_relacionados'] = Casos.objects.filter(categoria=self.object.categoria).exclude(id=self.object.id).order_by('-id')[:3]
		return context

class ListOrtopediaView(ListView):
	template_name = "casos_list.html"
	queryset = Casos.objects.filter(categoria=1).order_by('-id')

class ListTraumaView(ListView):
	template_name = "casos_list.html"
	queryset = Casos.objects.filter(categoria=2).order_by('-id')

class ListArtroscopiaView(ListView):
	template_name = "casos_list.html"
	queryset = Casos.objects.filter(categoria=3).order_by('-id')

class ListCirugia_BiologicaView(ListView):
	template_name = "casos_list.html"
	queryset = Casos.objects.filter(categoria=4).order_by('-id')

def contacto(request, template="contacto.html"):
	arreglo_mail = ['juancarlos@drvelezponce.com','drvelezponce@yahoo.com']
	if request.method == 'POST':
		form = EmailForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			phone = form.cleaned_data['phone']
			message = form.cleaned_data['message']
			try:
				subject, from_email, to = 'Una persona desea contactarlo en la web Dr. Velez Ponce', 'noreply@drvelezponce.com', arreglo_mail
				text_content = "Una persona desea contactarlo en la web Dr. Velez Ponce " + \
								'Nombre: ' + str(name) + ', '  + \
								'Telefono: ' + str( phone) + ', ' + \
								'Correo: ' + str(email) + ', ' + \
								'Mensaje: ' + str(message)

				html_content = "Una persona desea contactarlo en la web Dr. Velez Ponce " + \
								'Nombre: ' + str(name) + ', '  + \
								'Telefono: ' + str(phone) + ', ' + \
								'Correo: ' + str(email) + ', ' + \
								'Mensaje: ' + str(message)

				msg = EmailMultiAlternatives(subject, text_content, from_email, arreglo_mail)
				msg.attach_alternative(html_content, "text/html")
				msg.send()

				return HttpResponseRedirect('/')
			except:
				pass

	else:
		form = EmailForm()

	return render(request, template, locals())

class ListExpedientesView(ListView):
	template_name = "expedientes_list.html"
	queryset = Paciente.objects.all().order_by('-id')

def detail_expediente(request,slug='None'):
	template = "exp_detail.html"
	object = Paciente.objects.get(slug = slug)
	citas = Consulta.objects.filter(paciente = object).last()
	consultas = Consulta.objects.filter(paciente = object)

	#agregar nueva consulta
	if request.method == 'POST':
		form = ConsultaForm(request.POST)
		if form.is_valid():
			paciente = form.cleaned_data['paciente']
			fecha = form.cleaned_data['fecha']
			motivo = form.cleaned_data['motivo']
			examen_fisico = form.cleaned_data['examen_fisico']
			examen = form.cleaned_data['examen']
			tratamiento = form.cleaned_data['tratamiento']
			programacion_cita = form.cleaned_data['programacion_cita']
			costo = form.cleaned_data['costo']
			try:
				new_consulta = form.save(commit=False)
				new_consulta.paciente = paciente
				new_consulta.fecha = fecha
				new_consulta.motivo = motivo
				new_consulta.examen_fisico = examen_fisico
				new_consulta.examen = examen
				new_consulta.tratamiento = tratamiento
				new_consulta.programacion_cita = programacion_cita
				new_consulta.costo = costo
				new_consulta.save()

				return http.HttpResponseRedirect('')
			except:
				pass
	else:
		form = ConsultaForm()

	return render(request, template, locals())

class ListResumenesView(ListView):
	template_name = "resumen_clinico_list.html"
	queryset = ResumenClinico.objects.all().order_by('-id').distinct('paciente__nombre')

def detail_resumen(request,slug='None'):
	template = "resumen_clinico_detail.html"
	object = ResumenClinico.objects.filter(paciente__slug = slug)

	return render(request, template, locals())
