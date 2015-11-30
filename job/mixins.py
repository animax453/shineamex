#python imports

#django imports

#local imports

#inter app imports

#third party imports

class FormMixin(object):

	def __init__(self,**kwargs):
		if kwargs.get('job_id'):
			self.job_id = kwargs['job_id']
			kwargs.pop('job_id')
		return super(FormMixin,self).__init__(**kwargs)

	def clean(self):
		if not Job.objects.filter(id=int(self.job_id)):
			raise forms.ValidationError('Invalid Job Id')
		return super(FormMixin,self).clean()

	def clean_city(self):
		city = self.cleaned_data.get('city')
		if not city or not city.isdigit():
			raise forms.ValidationError('Invalid city value')

		if int(city)<0:
			raise forms.ValidationError('Invalid city value')
		return self.cleaned_data.get('city')