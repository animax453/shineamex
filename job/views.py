#python imports

#django imports
from django.http import Http404
from django.utils.text import slugify
from django.views.generic import ListView

#local imports
from models import Job

#inter app imports

#third party imports

class JobList(ListView):

	paginate_by = 10
	template_name = "job_list.html"

	def get_queryset(self):
		company_name = self.kwargs.get('company_name')
		company_id = self.kwargs.get('company_id')
		if company_name and company_id:
			jobs = Job.objects.select_related('recruiter').filter(recruiter__pk=company_id).order_by('edited_date')
			if not jobs:
				return jobs
			if slugify(jobs[0].recruiter.name) != company_name:
				raise Http404
			return jobs
		return Job.objects.all().select_related('recruiter').order_by('-edited_date')