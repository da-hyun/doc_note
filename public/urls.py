from django.urls import path
from .views import MedicalSearchView,MedicalSubjectsView,MedicalSurveyView


urlpatterns = [
    path('', MedicalSubjectsView.as_view(), name='subject'),
    path('survey/',MedicalSurveyView.as_view(), name='survey'),
    path('search/<int:pk>', MedicalSearchView.as_view(), name='public_search'),
]
