from django.db import models
from django.urls import reverse


class Doctor(models.Model):
    PATIENT_ID = models.IntegerField()
    CODE_NUMBER = models.IntegerField()
    CODE_DESCRIPTION = models.CharField(max_length=100)
    DATE = models.DateField(null=True)
    AGE = models.FloatField()
    GENDER = models.IntegerField()
    NOTES = models.CharField(max_length=900)
    CURRENTRX = models.CharField(max_length=100)
    DOSE = models.CharField(max_length=100)
    FREQUENCY = models.CharField(max_length=100)

    def __str__(self):
        return self.PATIENT_ID

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])


class DiagnosisNote(models.Model):
    note = models.TextField()
