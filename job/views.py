#python imports
from datetime import datetime, date

#django imports
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.utils.text import slugify
from django.views.generic import ListView, TemplateView, FormView, View
from django.forms.models import formset_factory

#local imports
from forms import JobApplicationForm, ReferralForm, RefreeForm
from models import Job, JobApplication, Refree

#inter app imports

#third party imports
import xlwt

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
		ReferralFormSet = formset_factory(ReferralForm,extra=1, max_num=3)
		context['referral_formset'] = ReferralFormSet()
		context['refree_form'] = RefreeForm()
		return context

	def save_refree_form(self):
		refree_email = self.request.POST.get('email')
		refree = Refree.objects.filter(email=refree_email)
		if refree:
			return refree[0],True

		refree_fields = ['name','email','contact_no','organization','city']
		refree_form_data = {field:self.request.POST.get(field) for field in refree_fields}
		refree_form = RefreeForm(refree_form_data)
		if refree_form.is_valid():
			return refree_form.save(),True
		else:
			return refree_form,False

	def render_form_errors(self,request):
		context = {}
		ReferralFormSet = formset_factory(ReferralForm,extra=1, max_num=3)
		context['referral_formset'] = ReferralFormSet(request.POST)
		context['refree_form'] = RefreeForm(request.POST)
		return render(request,self.template_name,context=context)


	def post(self,request,*args,**kwargs):
		# referral_formset = ReferralFormSet(request.POST)
		# refree_form = RefreeForm(request.POST)
		# if not referral_formset.is_valid() or not refree_form.is_valid():
		# 	return self.render_form_errors(request)
		
		refree,valid = self.save_refree_form()
		if not valid:
			return self.render_form_errors(request)
		total_forms = int(request.POST.get('form-TOTAL_FORMS',"1"))
		referral_form_list = []
		
		for i in range(0,total_forms):
			referral_form_data = {}
			referral_form_fields = ['name','email','contact_no','organization','city']
			for field in referral_form_fields:
				referral_form_data[field] = request.POST.get('form-'+str(i)+'-'+field)
			form_kwargs = {"job_id":kwargs.get('job_id'),"refree":refree}
			form_kwargs.update({"data":referral_form_data})
			referral_form = ReferralForm(**form_kwargs)
			if referral_form.is_valid():
				referral_form_list.append(referral_form)
			else:
				return self.render_form_errors(request)

		for form in referral_form_list:
			form.save()
		return HttpResponseRedirect("/thanks/")


class AppliesDownload(View):
	def get(self,request,*args,**kwargs):
		book = xlwt.Workbook(encoding='utf8')
		sheet = book.add_sheet('untitled')

		default_style = xlwt.Style.default_style
		datetime_style = xlwt.easyxf(num_format_str='dd/mm/yyyy hh:mm')
		date_style = xlwt.easyxf(num_format_str='dd/mm/yyyy')

		values_list = JobApplication.objects.all().values_list('name','email')

		for row, rowdata in enumerate(values_list):
			for col, val in enumerate(rowdata):
				# if isinstance(val, datetime):
				# 	style = datetime_style
				# elif isinstance(val, date):
				# 	style = date_style
				# else:
				# 	style = default_style

				sheet.write(row, col, val)

		response = HttpResponse(mimetype='application/vnd.ms-excel')
		response['Content-Disposition'] = 'attachment; filename=example.xls'
		book.save(response)
		return response

class ReferralsDownload(View):
	def get(self,request,*args,**kwargs):
		return HttpResponse("Hello World")





