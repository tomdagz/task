from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView
from .models import Plan
from .forms import PlanForm
# Create your views here.

class ListPlan(ListView):
	model = Plan
	template_name = 'plans.html'

class CreatePlan(CreateView):
	model = Plan
	form_class = PlanForm
	template_name = 'create_plan.html'
	success_url = '/admin'