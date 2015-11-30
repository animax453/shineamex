#python imports
from datetime import datetime

#django imports
from django.db import models

#local imports
from choices import *

#inter app imports
from company.models import Company

#third party imports

class Job(models.Model):
	title = models.CharField(max_length=250)
	salary = models.IntegerField(choices=SALARY_CHOICES,default=0)
	experience = models.IntegerField(choices=EXP_CHOICES,default=0)
	location = models.IntegerField(choices=LOCATION_CHOICES,default=0)
	farea = models.IntegerField(choices=FA_CHOICES,default=0)
	edited_date = models.DateTimeField(auto_now=True)
	recruiter = models.ForeignKey(Company)
	short_desc = models.CharField(max_length=200)
	description = models.TextField()

	class Meta:
		verbose_name_plural = "Jobs"

	def __unicode__(self):
		return self.title

class JobApplication(models.Model):
	name = models.CharField(max_length=50)
	contact_no = models.CharField(max_length=10)
	email = models.EmailField()
	organization = models.CharField(max_length=100)
	city = models.IntegerField(choices=CANDIDATE_CITY_CHOICES,default=0)
	application_date = models.DateTimeField(default=datetime.now)
	job_id = models.IntegerField()

class Refree(models.Model):
	name = models.CharField(max_length=50)
	contact_no = models.CharField(max_length=10)
	email = models.EmailField()
	organization = models.CharField(max_length=100)
	city = models.IntegerField(choices=CANDIDATE_CITY_CHOICES,default=0)

class JobReferral(models.Model):
	name = models.CharField(max_length=50)
	contact_no = models.CharField(max_length=10)
	email = models.EmailField()
	organization = models.CharField(max_length=100)
	city = models.IntegerField(choices=CANDIDATE_CITY_CHOICES,default=0)
	refree = models.ForeignKey(Refree)
	application_date = models.DateTimeField(default=datetime.now)
	job_id = models.IntegerField()




