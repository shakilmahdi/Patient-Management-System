from django.contrib import admin
from django.urls import path, include
from home import views  


urlpatterns = [
    path("", views.index, name='home'),
    path("services", views.services, name='services'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("appointment", views.appointment, name='appointment'),
    path("login", views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('signup', views.registerPage, name="register"),
    path('checkup', views.checkup, name="chekup"),
    path('OutdoorDoctor', views.OutdoorDoctor, name="outdoor docto"),
    path('HomePatient', views.HomePatient, name="home patient"),
    path('IndoorAdmission/', views.IndoorAdmission, name="indoor admission"),
    # path('saveenquiry', views.saveEnquiry, name="indoor saveenquiry"),
    # path('savedata', views.saveData, name="indoor savedata"),
    # path('saveindoordata', views.saveindoorData, name="indoor savedata"),
    #  path('saveoutdoordata', views.saveoutdoorData, name="outdoor savedata"),
    path('result', views.result, name="outdoor savedata"),
    path('update_contact/<str:pk>/', views.updatecontact, name="update_contact"),
    path('delete_contact/<int:pk>/', views.deletecontact, name="delete_contact"),
    path('update_outdoor/<str:pk>/', views.updateoutdoorpatient, name="update_outdoor"),
    path('delete_outdoor/<int:pk>/', views.deleteoutdoorpatient, name="delete_outdoor"),
    path('update_indoor/<str:pk>/', views.updateindoorpatient, name="update_indoor"),
    path('discharge_patient/<int:pk>/', views.dischargepatient, name="discharge_patient"),
    path('delete_indoor/<int:pk>/', views.deleteindoorpatient, name="update_indoor"),
    path('housePatient', views.housePatient, name=" housePatient"),
    path('report', views.report, name=" report"),
    path('addreport', views.addreport, name=" addreport"),
    path('indoorpatient', views.indoorpatient, name=" indoorpatient"),
    path('indoorad/', views.indoorad, name="indoorad"),
     path("dis_msg", views.dismsg, name="Discharge Message"),
    path("cmsg", views.cmsg, name=" Message"),
    path('amsg/<int:pk>/', views.amsg, name="Confirmatin Massege"),
    path("onlmsg", views.onlmsg, name=" Message"),
    path("Online_appointment", views.Online_appointment, name=" Online appointment"),
    path('HomePatientAppointment/', views.HomePatientAppointment, name="HomePatientAppointment"),
    # path('edit/<str:pk>/', views.edit, name=" edit"),
    
    # path('edit/<int:id>', views.edit, name=" edit"),
    
    # path("student", views.student, name='student'),

]