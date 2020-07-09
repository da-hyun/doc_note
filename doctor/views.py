from django.shortcuts import render
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from doctor.models import Doctor, DiagnosisNote
from .forms import output

class PatientListView(ListView):
    model = Doctor
    paginate_by = 15 # 한페이지에 출력 row

    def get_context_data(self, **kwargs):
        context = super(PatientListView, self).get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 10  # Display only 5 page numbers
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        return context

class PatientDetailView(DetailView):
    model = Doctor


class DiagnosisView(CreateView):
    model = DiagnosisNote
    fields = ['note']
    template_name = 'doctor/diagnosis.html'


def search(request):
    doctor_search = Doctor.objects.all()
    q = request.POST.get('q', "")
    if q:
        doctor_search = doctor_search.filter(PATIENT_ID=q) # __icontains
        return render(request, 'doctor/doctor_search.html', {'doctor_search': doctor_search, 'q': q})
    else:
        return render(request, 'doctor/doctor_search.html')

def diagnosis(request):
    q = request.POST.get('q', "")
    if q:
        obj = q
        top3 = output(obj)
        index = top3.index
        values = top3.values.reshape(3)
        return render(request, 'doctor/diagnosis_output.html', {'index': index, 'values': values,'obj':obj})
    else:
        return render(request, 'doctor/diagnosis.html')




