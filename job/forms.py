#python imports

#django imports
from django import forms
from django.forms import ModelForm

#local imports
from models import JobApplication

#inter app imports

#third party imports

class JobApplicationForm(ModelForm):

	city = forms.ChoiceField(max_length=24,widget=forms.Select(attrs={'class':'selectboxdiv'}))
	state = forms.ChoiceField(max_length=24,widget=forms.Select(attrs={'class':'selectboxdiv'}))
	
	class Meta:
		model = JobApplication
		fields = ['name','contact_no','email','organization','city','state']