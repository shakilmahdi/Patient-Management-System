from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    address = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    message =models.TextField()
    # comment = models.TextField()
    def __str__(self):
        return self.name

class Meta:
    db_table= Contact()

class AddReport(models.Model):
    report_name = models.CharField(max_length=122)
    report_category = models.CharField(max_length=122)
    report_description = models.TextField()
    report_file=models.FileField(upload_to='report/',blank=True)
    # comment = models.TextField()
    def __str__(self):
        return self.report_name
    




class Patient(models.Model):
    patient_type = models.CharField(max_length=122)
    patient_id = models.CharField(max_length=122)
    patient_date = models.DateField()
    patient_name = models.CharField(max_length=122)
    patient_gender = models.CharField(max_length=122)
    patient_age = models.CharField(max_length=122)
    patient_phone = models.CharField(max_length=122)
    patient_email = models.CharField(max_length=122)
    patient_dob = models.CharField(max_length=122)
    patient_blood_group = models.CharField(max_length=122)
    patient_national_ID = models.CharField(max_length=122)
    patient_marital_status = models.CharField(max_length=122)
    patient_guardian = models.CharField(max_length=122)
    patient_refered_by = models.CharField(max_length=122)
    patient_description = models.CharField(max_length=122)
    patient_address = models.CharField(max_length=122)
    patient_emergency_name = models.CharField(max_length=122)
    patient_emergency_relation = models.CharField(max_length=122)
    patient_emergency_contact = models.CharField(max_length=122)
    patient_emergency_address = models.CharField(max_length=122)
class Meta:
    db_table="Patient"
    # Report=models.FileField()
    # phone = models.CharField(max_length=12)


class OutdoorPatient(models.Model):
    date = models.DateField()
    branch = models.CharField(max_length=122)
    doctor = models.CharField(max_length=122)
    slot = models.CharField(max_length=122,blank=True)
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    age = models.CharField(max_length=122)
    gender = models.CharField(max_length=122)

# class Internal(models.Model):
#     a_date = models.DateField()
#     a_branch = models.CharField(max_length=122)
#     a_doctor = models.CharField(max_length=122)
   

class IndoorPatient(models.Model):
    indoor_treatment_patient_type = models.CharField(max_length=122)
    indoor_treatment_patient_id = models.CharField(max_length=122)
    patient_name = models.CharField(max_length=122)
    patient_age = models.CharField(max_length=122)
    patient_gender = models.CharField(max_length=122)
    patient_phone = models.CharField(max_length=122)
    indoor_patient_bed_bed_id = models.CharField(max_length=122)
    indoor_bed_category_name = models.CharField(max_length=122 )
    indoor_bed_price = models.CharField(max_length=122)
    indoor_patient_bed_entry_time = models.CharField(max_length=122)
    indoor_patient_bed_discharge_time = models.CharField(max_length=122)
    bed_total_bill = models.CharField(max_length=122)
    indoor_patient_doctor_doctor_id = models.CharField(max_length=122)
    doctor_specialization = models.CharField(max_length=122)
    doctor_visit_fee = models.CharField(max_length=122)
    indoor_patient_doctor_entry_time = models.CharField(max_length=122, blank=True)
    indoor_patient_doctor_discharge_time = models.CharField(max_length=122, blank=True)
    doctor_total_bill = models.CharField(max_length=122)
    outdoor_service_id = models.CharField(max_length=122)
    outdoor_service_rate = models.CharField(max_length=122)
    indoor_treatment_total_bill = models.CharField(max_length=122)
    indoor_treatment_discount_pc = models.CharField(max_length=122)
    indoor_treatment_total_bill_after_discount = models.CharField(max_length=122)
    indoor_treatment_total_paid = models.CharField(max_length=122)
    indoor_treatment_total_due = models.CharField(max_length=122)
    indoor_treatment_note = models.CharField(max_length=122)

    def __str__(self):
        return self.indoor_treatment_patient_id
    

   
class Appointment(models.Model):

    ap_date = models.DateField()
    ap_time = models.TimeField()
    ap_doctor = models.CharField(max_length=122)
    ap_name = models.CharField(max_length=122)
    ap_contact = models.CharField(max_length=122)

    
   