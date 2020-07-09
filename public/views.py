from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from public.models import Subject, Survey


class MedicalSubjectsView(ListView):
    model = Subject
    template_name = 'public/subject_list.html'

class MedicalSearchView(DetailView):
    model = Subject
    template_name = 'public/public_search.html'

class MedicalSurveyView(CreateView):
    model = Survey
    fields = ['survey']
    template_name = 'public/survey.html'



