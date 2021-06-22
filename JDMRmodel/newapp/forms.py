from django import forms
from .models import School,Address_Contacts,Admission_Details,Admission_Enquiry,admission

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = "__all__"

class AddressContactsForm(forms.ModelForm):
    class Meta:
        model = Address_Contacts
        fields = "__all__"

class AdmissionDetailsForm(forms.ModelForm):
    class Meta:
        model = Admission_Details
        fields = "__all__"

class AdmissionEnquiryForm(forms.ModelForm):
    class Meta:
        model = Admission_Enquiry
        fields = "__all__"

class admissionForm(forms.ModelForm):
    class Meta:
        model = admission
        fields = "__all__"