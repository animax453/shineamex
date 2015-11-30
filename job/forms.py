#python imports

#django imports
from django.forms import ModelForm

#local imports
from models import JobApplication

#inter app imports

#third party imports

class JobApplicationForm(ModelForm):
	
	class Meta:
		model = JobApplication
		fields = ['name','contact_no','email','organization','city']