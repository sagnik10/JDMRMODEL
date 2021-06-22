from django.shortcuts import render
from .models import School,Address_Contacts,Admission_Details,Admission_Enquiry,admission
from .forms import SchoolForm,AddressContactsForm,AdmissionDetailsForm,AdmissionEnquiryForm,admissionForm

def school(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid(): 
            form.save()        
            return render(request, 'success.html')
    else:
        form = SchoolForm()
    return render(request, 'school.html', {'form': form})

def AddressContacts(request):
    if request.method == 'POST':
        form = AddressContactsForm(request.POST)
        if form.is_valid(): 
            form.save()        
            return render(request, 'success.html')
    else:
        form = AddressContactsForm()
    return render(request, 'AddressContacts.html', {'form': form})

def AdmissionDetails(request):
    if request.method == 'POST':
        form = AdmissionDetailsForm(request.POST)
        if form.is_valid(): 
            form.save()        
            return render(request, 'success.html')
    else:
        form = AdmissionDetailsForm()
    return render(request, 'AdmissionDetails.html', {'form': form})

def AdmissionEnquiry(request):
    if request.method == 'POST':
        form = AdmissionEnquiryForm(request.POST)
        if form.is_valid(): 
            form.save()        
            return render(request, 'success.html')
    else:
        form = AdmissionEnquiryForm()
    return render(request, 'AdmissionEnquiry.html', {'form': form})

def Admission(request):
    if request.method == 'POST':
        form = admissionForm(request.POST)
        if form.is_valid(): 
            form.save()        
            return render(request, 'success.html')
    else:
        form = admissionForm()
    return render(request, 'admission.html', {'form': form})