from django.urls import path
from .views import *

urlpatterns = [
    path('', PatientListView.as_view(), name='list'),
    path('diagnosis/', DiagnosisView.as_view(), name='diagnosis'),
    path('detail/<int:pk>', PatientDetailView.as_view(), name='detail'),
    path('search', search, name='doctor_search'),
    path('output', diagnosis, name='diagnosis_output')
]