#python imports

#django imports
from django import forms
from django.forms import ModelForm

#local imports
from choices import *
from models import JobApplication, Job

#inter app imports

#third party imports

class JobApplicationForm(ModelForm):

	city = forms.ChoiceField(choices=CANDIDATE_CITY_CHOICES,widget=forms.Select(attrs={'class':'selectboxdiv'}))
	state = forms.ChoiceField(choices=CANDIDATE_STATE_CHOICES,widget=forms.Select(attrs={'class':'selectboxdiv'}))
	
	class Meta:
		model = JobApplication
		fields = ['name','contact_no','email','organization','city','state']

	def __init__(self,**kwargs):
		if kwargs.get('job_id'):
			self.job_id = kwargs['job_id']
			kwargs.pop('job_id')
		return super(JobApplicationForm,self).__init__(**kwargs)

	def clean(self):
		if not Job.objects.filter(id=int(self.job_id)):
			raise forms.ValidationError('Invalid Job Id')
		return super(JobApplicationForm,self).clean()

	def save(self,commit=True):
		apply_job = super(JobApplicationForm,self).save(False)
		setattr(apply_job,'job_id',int(self.job_id))
		apply_job.save()
		return apply_job 