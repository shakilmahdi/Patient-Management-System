from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm  


from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from home.models import Contact
from home.models import Patient
from home.models import IndoorPatient
from home.models import OutdoorPatient
from home.models import AddReport
from home.models import Appointment

# from .filter import PatientFilter

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from home import forms as homeform

def index(request):
	 return render(request, 'index.html')
	 
def cmsg(request):
	 return render(request, 'contact_message.html')

def onlmsg(request):
	return render(request, 'oamsg.html')

def dismsg(request):
	return render(request, 'c_discharge.html')

def indoorad(request):
	 return render(request, 'indoorad.html')

def appointment(request):
	 if request.user.is_anonymous:
		 return redirect("login")
	 return render(request,'appointment.html') 


def signup(request):
	 return render(request, 'register.html', context)


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('/login')
	else:
		form = homeform.CreateUserForm()
		if request.method == 'POST':
			form = homeform.CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('/login')
			

		context = {'form':form}
		return render(request, 'register.html', context)



def logoutUser(request):
	 logout(request)
	 return redirect ("/login")


def updatecontact(request):
	 return render (request, 'updatecontact.html')

@csrf_exempt
def indoorpatient(request):
	IndoorAdmission = IndoorPatient.objects.all()

	context= {'IndoorAdmission':IndoorAdmission,}
	
	return render (request, 'indoorpatient.html',context)

def services(request):
	 return render (request, 'services.html')
 
def about(request):
	 return render (request, 'about.html')

@csrf_exempt
def HomePatientAppointment(request):

	form = homeform.HpAppointmentForm()
	print("ok")
	if request.method == 'POST':
		
		form = homeform.HpAppointmentForm(request.POST)
		print(form.errors.as_data())
		if form.is_valid():
			form.save()
			return redirect('/onlmsg')
			
	context = {'form':form}
	return render (request, 'in_appointment.html')


@csrf_exempt
def dischargepatient(request,pk):
		IndoorAdmission= IndoorPatient.objects.get(id=pk)
	

		context = {'IndoorAdmission': IndoorAdmission,}
		return render (request, 'dischargeindoorpatient.html', context)		
	
def checkup(request):
	 return render (request, 'checkup.html')

def appointment(request):
	 return render(request,'appointment.html') 

def updatecontact(request):
	 return render(request,'updatecontact.html') 


def report(request):
	new=AddReport.objects.all()
	context= {'new': new,}
	return render (request, 'report.html',context)

def Online_appointment(request):
	new2 = Appointment.objects.all()
	context= {'new2': new2,}
	return render (request, 'Online_appointment.html',context)
	
def result(request):
	IndoorAdmission = IndoorPatient.objects.all()
	HomePatient = Patient.objects.all()
	OutdoorDoctor =OutdoorPatient.objects.all()
	contact = Contact.objects.all()
	new2 = Appointment.objects.all()
	# student = Student.object.all()
	context= {'new2': new2,'IndoorAdmission':IndoorAdmission,'HomePatient':HomePatient,'OutdoorDoctor':OutdoorDoctor,'contact':contact,}
	return render (request, 'result.html',context)
		 	
@csrf_exempt
def loginPage(request):
	 
	if request.user.is_authenticated:
		return redirect('/appointment')
		  
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('appointment')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)


def appointment(request):
	 	# return render(request,'housePatient.html') 
		IndoorAdmission = IndoorPatient.objects.all()
		HomePatient = Patient.objects.all()
		OutdoorDoctor =OutdoorPatient.objects.all()
		contact = Contact.objects.all()
		context= {'IndoorAdmission':IndoorAdmission,'HomePatient':HomePatient,'OutdoorDoctor':OutdoorDoctor,'contact':contact}
		return render(request, 'appointment.html', context)


@csrf_exempt
def housePatient(request):
		if request.user.is_anonymous:
			return redirect("login")
		if request.method=="POST":
			fromdate=request.POST.get('fromdate')
			todate=request.POST.get('todate')
			searchresult=Patient.objects.raw('select patient_name, patient_phone, patient_gender, patient_age,patient_blood_group, patient_description, patient_date from Patient where patient_date between "'+fromdate+'" and "'+todate+'"' )
			return render(request, 'housePatient.html', {'Patient':searchresult})
		else:
			HomePatient = Patient.objects.all()
		

		# myFilter=PatientFilter()

		context= {'HomePatient':HomePatient,}
		return render(request, 'housePatient.html', context)




@csrf_exempt
def HomePatient(request):

	form = homeform.HomePatientForm()
	if request.method == 'POST':
		form = homeform.HomePatientForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/housePatient')
			
	context = {'form':form}
	return render(request, 'HomePatient.html', context)
	
@csrf_exempt
def amsg(request,pk):
		OutdoorDoctor= OutdoorPatient.objects.get(id=pk)
		context = {'OutdoorDoctor': OutdoorDoctor,}
		return render (request, 'amsg.html', context)		
	

@csrf_exempt
def OutdoorDoctor(request):
		form = homeform.OutdoorDoctorForm()
		if request.method == 'POST':
			
			form = homeform.OutdoorDoctorForm(request.POST)
			if form.is_valid():
				obj = form.save()
				last_id = obj.pk
				return redirect('/amsg/'+str(obj.pk), pk=last_id)
			
		context = {'form':form}
		return render(request, 'OutdoorDoctor.html', context)


@csrf_exempt
def IndoorAdmission(request):
		form = homeform.IndoorAdmissionForm()
		print()
		if request.method == 'POST':
			form = homeform.IndoorAdmissionForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('/indoorpatient')
			

		context = {'form':form}
		return render(request, 'IndoorAdmission.html', context)



def contact(request):
		form = homeform.ContactForm()
		if request.method == 'POST':
			form = homeform.ContactForm(request.POST)
			if form.is_valid():
				# if Contact.objects.filter(name=name, email=email, message=message).exists():
				# 	raise forms.ValidationError("This data already exists in the database")

				form.save()
				return redirect('/cmsg')
			

		context = {'form':form}
		
		return render(request, 'contact.html', context)




@csrf_exempt

def deletecontact(request, pk):
  contact = Contact.objects.get(id=pk)
  contact.delete()
  return redirect('/result')	


@csrf_exempt
def updatecontact(request, pk):
		contact= Contact.objects.get(id=pk)
		form = homeform.ContactForm(instance=contact)
		if request.method == 'POST':
			form = homeform.ContactForm(request.POST, instance=contact)
			if form.is_valid():
				form.save()
				return redirect('/result')

		context = {'contact': contact,}
		return render (request, 'updatecontact.html', context)



def deleteoutdoorpatient(request, pk):
  OutdoorDoctor = OutdoorPatient.objects.get(id=pk)
  OutdoorDoctor.delete()
  return redirect('/result')	


@csrf_exempt
def updateoutdoorpatient(request, pk):
		OutdoorDoctor= OutdoorPatient.objects.get(id=pk)
		form = homeform.OutdoorDoctorForm(instance=OutdoorDoctor)
		if request.method == 'POST':
			form = homeform.OutdoorDoctorForm(request.POST, instance=OutdoorDoctor)
			if form.is_valid():
				form.save()
				return redirect('/result')

		context = {'OutdoorDoctor': OutdoorDoctor,}
		return render (request, 'OutdoorDoctor.html', context)


def deleteindoorpatient(request, pk):
  IndoorAdmission = IndoorPatient.objects.get(id=pk)
  IndoorAdmission.delete()
  return redirect('/result')	


@csrf_exempt
def updateindoorpatient(request, pk):
		IndoorAdmission= IndoorPatient.objects.get(id=pk)
		form = homeform.IndoorAdmissionForm(instance=IndoorAdmission)
		if request.method == 'POST':
			form = homeform.IndoorAdmissionForm(request.POST, instance=IndoorAdmission)
			if form.is_valid():
				form.save()
				return redirect('/result')

		context = {'IndoorAdmission': IndoorAdmission,}
		return render (request, 'IndoorAdmission.html', context)		
	




@csrf_exempt
def addreport(request):

	form = homeform.AddReportForm()
	if request.method == 'POST':
		form = homeform.AddReportForm(request.POST, request.FILES)
		if form.is_valid():
		
			print("ok")
			
			form.save()
			return redirect('/report')
			
	context = {'form':form}
	return render(request, 'addreport.html', context)































# old format



	 
# def contact(request):
# 	return render (request, 'contact.html')

# def HomePatient(request):
# 	 return render (request, 'HomePatient.html')
# def saveEnquiry(request):
# 	if request.method=="POST":
# 		name=request.POST.get('name')
# 		email=request.POST.get('email')
# 		address=request.POST.get('address')
# 		phone=request.POST.get('phone')
# 		message=request.POST.get('message')
# 		# comment=request.POST.get('comment')
# 		en=Contact(name=name,email=email,address=address, phone=phone,message=message)
# 		en.save()
# 	return render (request, 'contact.html')



# def OutdoorDoctor(request):
# 	 return render (request, 'OutdoorDoctor.html')

 






# @csrf_exempt
# def saveoutdoorData(request):
# 	if request.method=="POST":
# 		patient_name=request.POST.get('patient_name')
# 		patient_gender=request.POST.get('patient_gender')
# 		patient_age=request.POST.get('patient_age')
# 		patient_phone=request.POST.get('patient_phone')
# 		patient_email=request.POST.get('patient_email')
# 		patient_dob=request.POST.get('patient_dob')
# 		patient_blood_group=request.POST.get('patient_blood_group')
# 		patient_national_ID=request.POST.get('patient_national_ID')
# 		patient_marital_status=request.POST.get('patient_marital_status')
# 		patient_guardian=request.POST.get('patient_guardian')
# 		patient_refered_by=request.POST.get('patient_refered_by')
# 		patient_description=request.POST.get('patient_description')
# 		patient_address=request.POST.get('patient_address')
# 		patient_emergency_name=request.POST.get('patient_emergency_name')
# 		patient_emergency_relation=request.POST.get('patient_emergency_relation')
# 		patient_emergency_contact=request.POST.get('patient_emergency_contact')
# 		patient_emergency_address=request.POST.get('patient_emergency_address')
		
# 		ep=OutdoorPatient(patient_name=patient_name, patient_gender=patient_gender,patient_age=patient_age,patient_phone=patient_phone,patient_email=patient_email,patient_dob=patient_dob,patient_blood_group=patient_blood_group,patient_national_ID=patient_national_ID,patient_marital_status=patient_marital_status, patient_guardian=patient_guardian,patient_refered_by=patient_refered_by,patient_description=patient_description,patient_address=patient_address,patient_emergency_name=patient_emergency_name,patient_emergency_relation=patient_emergency_relation,patient_emergency_contact=patient_emergency_contact,patient_emergency_address=patient_emergency_address)
# 		ep.save()
# 	return render (request,'test.html')

# def IndoorAdmission(request):
# 	 return render (request, 'IndoorAdmission.html')
# def saveindoorData(request):
# 	 return render (request, 'IndoorAdmission.html')

# @csrf_exempt
# def saveindoorData(request):
# 	if request.method=="POST":
# 		indoor_treatment_patient_id=request.POST.get('indoor_treatment_patient_id')
# 		patient_name=request.POST.get('patient_name')
# 		patient_gender=request.POST.get('patient_gender')
# 		patient_age=request.POST.get('patient_age')
# 		patient_phone=request.POST.get('patient_phone')
# 		indoor_bed_category_name=request.POST.get('indoor_bed_category_name')
# 		indoor_patient_bed_bed_id=request.POST.get('indoor_patient_bed_bed_id')
# 		indoor_bed_price=request.POST.get('indoor_bed_price')
# 		indoor_patient_bed_entry_time=request.POST.get('indoor_patient_bed_entry_time')
# 		indoor_patient_bed_discharge_time=request.POST.get('indoor_patient_bed_discharge_time')
# 		bed_total_bill=request.POST.get('bed_total_bill')
# 		indoor_patient_doctor_doctor_id=request.POST.get('indoor_patient_doctor_doctor_id')
# 		doctor_specialization=request.POST.get('doctor_specialization')
# 		doctor_visit_fee=request.POST.get('doctor_visit_fee')
# 		doctor_total_bill=request.POST.get('doctor_total_bill')
# 		indoor_service_id=request.POST.get('indoor_service_id')
# 		indoor_service_rate=request.POST.get('indoor_service_rate')
# 		indoor_treatment_total_bill=request.POST.get('indoor_treatment_total_bill')
# 		indoor_treatment_discount_pc=request.POST.get('indoor_treatment_discount_pc')
# 		indoor_treatment_total_bill_after_discount=request.POST.get('indoor_treatment_total_bill_after_discount')
# 		indoor_treatment_total_paid=request.POST.get('indoor_treatment_total_paid')
# 		indoor_treatment_total_due=request.POST.get('indoor_treatment_total_due')
# 		indoor_treatment_payment_type=request.POST.get('indoor_treatment_payment_type')
# 		indoor_treatment_payment_type_no=request.POST.get('indoor_treatment_payment_type_no')
# 		indoor_treatment_note=request.POST.get('indoor_treatment_note')
		
		
# 		ex=IndoorPatient(indoor_treatment_patient_id=indoor_treatment_patient_id,patient_name=patient_name, patient_gender=patient_gender,patient_age=patient_age,patient_phone=patient_phone,indoor_bed_category_name=indoor_bed_category_name,indoor_patient_bed_bed_id=indoor_patient_bed_bed_id,indoor_bed_price=indoor_bed_price,indoor_patient_bed_entry_time=indoor_patient_bed_entry_time,indoor_patient_bed_discharge_time=indoor_patient_bed_discharge_time,bed_total_bill=bed_total_bill,indoor_patient_doctor_doctor_id=indoor_patient_doctor_doctor_id,doctor_specialization=doctor_specialization,doctor_visit_fee=doctor_visit_fee,doctor_total_bill=doctor_total_bill,indoor_service_id=indoor_service_id,indoor_service_rate=indoor_service_rate,indoor_treatment_total_bill=indoor_treatment_total_bill,indoor_treatment_discount_pc=indoor_treatment_discount_pc,indoor_treatment_total_bill_after_discount=indoor_treatment_total_bill_after_discount,indoor_treatment_total_paid=indoor_treatment_total_paid,indoor_treatment_total_due=indoor_treatment_total_due, indoor_treatment_payment_type=indoor_treatment_payment_type,indoor_treatment_payment_type_no=indoor_treatment_payment_type_no,indoor_treatment_note=indoor_treatment_note)
# 		ex.save()
# 	return render (request,'test.html')

# def HomePatient(request):
# 	if request.user.is_anonymous:
# 		return redirect("login")
# 	 return render(request,'HomePatient.html') 	
# def saveData(request):
# 	 return render (request, 'HomePatient.html') 
# @csrf_exempt
# def saveData(request):
# 	if request.method=="POST":
# 		branch=request.POST.get('branch')
# 		speciality=request.POST.get('speciality')
# 		doctor=request.POST.get('doctor')
# 		notes=request.POST.get('notes')
# 		name=request.POST.get('name')
# 		phone=request.POST.get('phone')
# 		age=request.POST.get('age')
# 		gender=request.POST.get('gender')
# 		es=Patient(branch=branch, speciality=speciality,doctor=doctor,notes=notes,name=name,age=age,phone=phone,gender=gender)
# 		es.save()
# 	return render (request,'test.html')

# def saveEnquiry(request):
# 	 return render (request, 'contact.html')




# def saveoutdoorData(request):
# 	 return render (request, 'OutdoorAdmission.html')
	

# @csrf_exempt
# def student(request):
# 		form = homeform.StudentForm()
# 		if request.method == 'POST':
# 			form = homeform.StudentForm(request.POST)
# 			if form.is_valid():
# 				form.save()
# 				return redirect('/student')
			

# 		context = {'form':form}
		
# 		return render(request, 'student.html', context)


# def updatecontact(request,pk):

# 		contact= Contact.objects.get(id=pk)
# 		form = homeform.ContactForm(instance=contact)
# 		if request.method == 'POST':
# 			form = homeform.ContactForm(request.POST, instance=contact)
# 			if form.is_valid():
# 				form.save()
# 				return redirect('/result')
# 		# context = {'form':form}
# 		context = {"name" : "sadik"}
# 		return render(request, 'contact.html', context)

