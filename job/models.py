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
	contact_no = models.IntegerField()
	email = models.EmailField()
	organization = models.CharField(max_length=100)
	city = models.IntegerField(choices=CANDIDATE_CITY_CHOICES,default=0)
	application_date = models.DateTimeField(default=datetime.now)

