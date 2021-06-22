from django.urls import path
from . import views

urlpatterns = [
    path('',views.school),
    path('AddressContacts/',views.AddressContacts),
    path('AdmissionDetails/',views.AdmissionDetails),
    path('AdmissionEnquiry/',views.AdmissionEnquiry),
    path('admission/',views.Admission)
]