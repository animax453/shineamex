#python imports

#django imports
from django import forms
from django.forms import ModelForm

#local imports
from choices import *
from models import JobApplication, JobReferral, Refree

#inter app imports

#third party imports

class JobApplicationForm(ModelForm):

	city = forms.ChoiceField(initial="-1",choices=CANDIDATE_CITY_CHOICES,widget=forms.Select(attrs={'class':'selectboxdiv'}))
	
	class Meta:
		model = JobApplication
		fields = ['name','contact_no','email','organization','city']

	def __init__(self,**kwargs):
		if kwargs.get('job_id'):
			self.job_id = kwargs['job_id']
			kwargs.pop('job_id')
		return super(JobApplicationForm,self).__init__(**kwargs)

	def clean(self):
		if not Job.objects.filter(id=int(self.job_id)):
			raise forms.ValidationError('Invalid Job Id')
		return super(JobApplicationForm,self).clean()

	def clean_city(self,city):
		if city<0:
			raise forms.ValidationError('Invalid city value')

	def clean_state(self,city):
		if city<0:
			raise forms.ValidationError('Invalid state value')

	def save(self,commit=True):
		apply_job = super(JobApplicationForm,self).save(False)
		setattr(apply_job,'job_id',int(self.job_id))
		apply_job.save()
		return apply_job 


class RefreeForm(JobApplicationForm):

	class Meta:
		model = Refree
		fields = ['name','contact_no','email','organization','city']

	def save(self,commit=True):
		return super(JobApplicationForm,self).save(commit)

class ReferralForm(JobApplicationForm):

	class Meta:
		model = JobReferral
		fields = ['name','contact_no','email','organization','city']

