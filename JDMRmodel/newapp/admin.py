from django.contrib import admin
from .models import School,Address_Contacts,admission,Admission_Details,Admission_Enquiry

admin.site.register(School)
admin.site.register(Address_Contacts)
admin.site.register(admission)
admin.site.register(Admission_Details)
admin.site.register(Admission_Enquiry)
