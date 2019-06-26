# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from college_erp.models import login, signup, student, department, subject, college, faculty
from college_erp.serializers import LoginSerializer, SignupSerializer, StudentSerializer, SubjectSerializer, FacultySerializer, DepartmentSerializer, CollegeSerializer 
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from datetime import datetime

class loginList(APIView):
    def get(self, request, format=None):
        login_data = login.objects.all()
        serializer = LoginSerializer(login_data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class signupList(APIView):
    def get(self, request, format=None):
        signup_data = signup.objects.all()
        serializer = SignupSerializer(signup_data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print request.data
        date = request.data.get('dob', None)
        print date
        # formatedDate = date.strftime("%Y-%m-%d %H:%M:%S")
        # print formatedDate
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: print serializer.errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class studentList(APIView):
    def get(self, request, format=None):
        student_data = student.objects.all()
        serializer = StudentSerializer(student_data, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serialzer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class departmentList(APIView):
    def get(self, request, format=None):
        deptt_data = department.objects.all()
        serializer = DepartmentSerializer(deptt_data, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = DepartmentSerializer(data=request.data)
        if serialzer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class facultyList(APIView):
    def get(self, request, format=None):
        fac_data = faculty.objects.all()
        serializer = FacultySerializer(fac_data, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = FacultySerializer(data=request.data)
        if serialzer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class subjectList(APIView):
    def get(self, request, format=None):
        sub_data = subject.objects.all()
        serializer = SubjectSerializer(sub_data, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = SubjectSerializer(data=request.data)
        if serialzer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class collegeList(APIView):
    def get(self, request, format=None):
        col_data = college.objects.all()
        serializer = CollegeSerializer(col_data, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CollegeSerializer(data=request.data)
        if serialzer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)









'''
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


@csrf_exempt
def signup_list(request):
    if request.method == 'GET':
        erp = signup.objects.all()
        serializer = SignupSerializer(erp, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SignupSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def lecture_list(request):
    if request.method == 'GET':
        erp = lecture.objects.all()
        serializer = LectureSerializer(erp, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        lecture_data = JSON().parse(request)
        serializer = LectureSerializer(data=lecture_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
'''