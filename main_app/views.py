from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Verbiage
from .forms import EtymolodyForm


class VerbiageList(ListView):
    model = Verbiage
    template_name = 'verbiages/index.html'


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def verbiages_detail(request, verbiage_id):
    verbiage = Verbiage.objects.get(id=verbiage_id)
    etymology_form = EtymolodyForm()
    return render(request, 'verbiages/detail.html', { 'verbiage': verbiage, "etymology_form": etymology_form })


class VerbiageCreate(CreateView):
    model = Verbiage
    fields = '__all__'


class VerbiageUpdate(UpdateView):
  model = Verbiage
  fields = '__all__'


class VerbiageDelete(DeleteView):
  model = Verbiage
  success_url = '/verbiages/'