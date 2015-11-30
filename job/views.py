#python imports

#django imports
from django.http import Http404, HttpResponseRedirect
from django.utils.text import slugify
from django.views.generic import ListView, TemplateView, FormView

#local imports
from forms import JobApplicationForm
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

class JobDetail(TemplateView):

	template_name = "job_detail.html"
	job = None

	def redirect_path(self):
		if self.kwargs.get('job_title') != slugify(self.job.title):
			return "/job/"+slugify(self.job.title)+"/"+str(self.job.id)+"/"

	def get(self,request,*args,**kwargs):
		job_id = int(kwargs.get('job_id'))
		job_title = kwargs.get('job_title')
		job = Job.objects.filter(id=job_id)
		if not job:
			raise Http404
		self.job = job[0]

		redirect_path = self.redirect_path()
		if redirect_path:
			return HttpResponseRedirect(redirect_path)
		return super(JobDetail,self).get(request,*args,**kwargs)


	def get_context_data(self,**kwargs):
		context = super(JobDetail,self).get_context_data(**kwargs)
		context['job'] = self.job
		return context

class JobApplicationView(FormView):
	template_name = "application.html"
	form_class = JobApplicationForm

