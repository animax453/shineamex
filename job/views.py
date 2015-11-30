#python imports

#django imports
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.utils.text import slugify
from django.views.generic import ListView, TemplateView, FormView, View
from django.forms.models import formset_factory

#local imports
from forms import JobApplicationForm, ReferralForm, RefreeForm
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
	success_url = "/thanks/"

	def get_form_kwargs(self):
		kwargs = super(JobApplicationView,self).get_form_kwargs()
		kwargs['job_id'] = self.kwargs.get('job_id')
		return kwargs

	def form_valid(self,form):
		form.save()
		if not self.request.session.get('applied_jobs'):
			self.request.session['applied_jobs'] = [int(self.kwargs.get('job_id'))]
		else:
			self.request.session['applied_jobs'] = self.request.session['applied_jobs'].append(int(self.kwargs.get('job_id')))

		return super(JobApplicationView,self).form_valid(form)


class ThanksView(TemplateView):

	template_name = "thanks.html"

	def get_context_data(self,**kwargs):
		context = super(ThanksView,self).get_context_data(**kwargs)
		applied_jobs_list = self.request.session.get('applied_jobs',[])
		context['jobs'] = Job.objects.exclude(id__in=applied_jobs_list).order_by('-edited_date')
		return context


class ReferView(TemplateView):

	template_name = "refer.html"

	def get_context_data(self,**kwargs):
		context = super(ReferView,self).get_context_data(**kwargs)
		ReferralFormSet = formset_factory(ReferralForm,extra=1, max_num=5)
		context['referral_formset'] = ReferralFormSet()
		context['refree_form'] = ReferralForm()
		return context

class AppliesDownload(View):
	def get(self,request,*args,**kwargs):
		return HttpResponse("Hello World")

class ReferralsDownload(View):
	def get(self,request,*args,**kwargs):
		return HttpResponse("Hello World")





