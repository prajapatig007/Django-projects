from rest_framework import serializers
from college_erp.models import login, signup, student, subject, college, faculty, department


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = login
        fields = ('username', 'password')

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = signup
        fields = ('first_name', 'last_name', 'contact', 'email', 'dob','gender')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ('roll_no', 'first_name', 'last_name', 'dob', 'gender', 'phone', 'email', 'address')

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = department
        fields = ('deptt_id', 'deptt_name', 'deptt_head')

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = faculty
        fields = ('fac_id', 'fac_first_name', 'fac_last_name', 'fac_dob', 'fac_gender', 'fac_phone', 'fac_email', 'fac_address')

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = college
        fields = ('col_id', 'col_name', 'col_phone', 'col_email', 'col_address', 'col_website')

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = subject
        fields = ('sub_id', 'sub_name')