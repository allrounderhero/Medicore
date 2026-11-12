from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    Date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specilization = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Appoinment(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    appoinment_date = models.DateField()
    reason =  models.TextField()
    def __str__(self):
        return f"{self.patient} - {self.doctor}"
# Create your models here.
