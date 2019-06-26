# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
GENDER_CHOICES = (
        ('M', 'male'),
        ('F', 'female'),
    )

class login(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=10)

    class Meta:
        pass

class signup(models.Model):
    first_name = models.CharField(max_length=30, default = None, null=True, blank=False)
    last_name = models.CharField(max_length=30, default = None, null=True, blank=False)
    contact = models.CharField(max_length=12, unique=True, null=True, blank=False, default=None)
    email = models.CharField(max_length=100, default = None, null=True, blank=False)
    gender = models.CharField(max_length=4, choices=GENDER_CHOICES, default = None, null=True, blank=False)
    dob = models.DateField(default = None, null=False, blank=False)

    class Meta:
        pass

class student(models.Model):
    roll_no = models.IntegerField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateTimeField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=None)
    phone = models.CharField(max_length=12, blank=False, unique=True, null=False)
    email = models.EmailField()
    address = models.CharField(max_length=100)

    class Meta:
        pass

class department(models.Model):
    deptt_id = models.CharField(max_length=30, unique=True, primary_key=True)
    deptt_name = models.CharField(max_length=30)
    deptt_head = models.CharField(max_length=30)
    class Meta:
        pass

class faculty(models.Model):
    fac_id = models.CharField(max_length=30, unique=True, primary_key=True)
    fac_first_name = models.CharField(max_length=30)
    fac_last_name = models.CharField(max_length=30)
    fac_phone = models.CharField(max_length=12, unique=True, null=False, blank=False)
    fac_email = models.EmailField()
    fac_address = models.CharField(max_length=50)
    fac_dob = models.DateTimeField()
    fac_gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default = None)
    class Meta:
        pass

class subject(models.Model):
    sub_id = models.CharField(max_length=10, unique=True)
    sub_name = models.CharField(max_length=30)

    class Meta:
        pass

class college(models.Model):
    col_id = models.CharField(max_length=10, unique=True)
    col_name = models.CharField(max_length=50)
    col_phone = models.CharField(max_length=12, unique=True, blank=False, null=False)
    col_email = models.EmailField()
    col_address = models.CharField(max_length=50)
    col_website = models.CharField(max_length=50, unique=True)

    class Meta:
        pass