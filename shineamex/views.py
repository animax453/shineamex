#python imports

#django imports
from django.views.generic import TemplateView

#local imports

#inter app imports
from job.models import Job

#third party imports

class Home(TemplateView):

	template_name = "index.html"

	def get_context_data(self,**kwargs):
		context = super(Home,self).get_context_data(**kwargs)
		jobs = Job.objects.all()
		if jobs:
			context['recruiter'] = jobs[0].recruiter
		context['jobs'] = jobs
		return context
