#python imports

#django imports
from django import forms
from django.forms import ModelForm

#local imports
from choices import *
from mixins import FormMixin
from models import JobApplication, JobReferral, Refree, Job

#inter app imports

#third party imports

class JobApplicationForm(FormMixin,ModelForm):

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

	def clean_city(self):
		city = self.cleaned_data.get('city')
		if not city or not city.isdigit():
			raise forms.ValidationError('Invalid city value')

		if int(city)<0:
			raise forms.ValidationError('Invalid city value')
		return self.cleaned_data.get('city')

	def save(self,commit=True):
		apply_job = super(JobApplicationForm,self).save(False)
		setattr(apply_job,'job_id',int(self.job_id))
		apply_job.save()
		return apply_job 


class RefreeForm(FormMixin,ModelForm):
	city = forms.ChoiceField(initial="-1",choices=CANDIDATE_CITY_CHOICES,widget=forms.Select(attrs={'class':'selectboxdiv'}))
	class Meta:
		model = Refree
		fields = ['name','contact_no','email','organization','city']

class ReferralForm(FormMixin,ModelForm):

	city = forms.ChoiceField(initial="-1",choices=CANDIDATE_CITY_CHOICES,widget=forms.Select(attrs={'class':'selectboxdiv cls_referral_city'}))
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'cls_referral_name','maxlength':100}))
	contact_no = forms.CharField(widget=forms.TextInput(attrs={'class':'cls_referral_contactnum','maxlength':10}))
	email = forms.CharField(widget=forms.TextInput(attrs={'class':'cls_referral_email','maxlength':100}))
	organization = forms.CharField(widget=forms.TextInput(attrs={'class':'cls_referral_org','maxlength':200}))

	class Meta:
		model = JobReferral
		fields = ['name','contact_no','email','organization','city']

	def save(self,commit=True):
		apply_job = super(JobApplicationForm,self).save(False)
		setattr(apply_job,'job_id',int(self.job_id))
		apply_job.save()
		return apply_job 

