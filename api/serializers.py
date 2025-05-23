from rest_framework import serializers
from .models import Patient, Doctor, PatientDoctorMapping


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'contact_number', 'address']

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'specialization', 'contact_number', 'email']

class PatientDoctorMappingSerializer(serializers.ModelSerializer):

    patient = PatientSerializer()
    doctor = DoctorSerializer()

    
    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient', 'doctor', 'assigned_date']


