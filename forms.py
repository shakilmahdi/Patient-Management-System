from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from home import models as homeModel



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class ContactForm(ModelForm):
	class Meta:
		model = homeModel.Contact
		fields = '__all__'

	def clean(self):
		cleaned_data = super().clean()
		name = cleaned_data.get('name')
		if  homeModel.Contact.objects.filter(name=name).exists():
			self.add_error('name', 'Username already exists')


class HomePatientForm(ModelForm):
	class Meta:
		model = homeModel.Patient
		fields = '__all__' 

	def clean(self):
		cleaned_data = super().clean()
		patient_national_ID = cleaned_data.get('patient_national_ID')
		if  homeModel.Patient.objects.filter(patient_national_ID=patient_national_ID).exists():
			self.add_error('patient_national_ID', 'Username already exists')


class IndoorAdmissionForm(ModelForm):
	class Meta:
		model = homeModel.IndoorPatient
		fields = '__all__' 

class OutdoorDoctorForm(ModelForm):
	class Meta:
		model = homeModel.OutdoorPatient
		fields = '__all__'

class AddReportForm(ModelForm):
	class Meta:
		model = homeModel.AddReport
		fields = '__all__'

class HpAppointmentForm(ModelForm):
	class Meta:
		model = homeModel.Appointment
		fields = '__all__'