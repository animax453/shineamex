#python imports

#django imports
from django.conf.urls import url
from django.contrib import admin

#local imports
from views import ReferralsDownload, AppliesDownload
from models import Job, JobApplication

#inter app imports

#third party imports

class JobAdmin(admin.ModelAdmin):
	exclude = ('edited_date',)

admin.site.register(Job,JobAdmin)

class JobApplicationAdmin(admin.ModelAdmin):
	
	def get_urls(self):
		urls = super(JobApplicationAdmin,self).get_urls()
		urls = urls+[
            url(r'^applies/download/$',AppliesDownload.as_view()),
            url(r'^referrals/download/$',ReferralsDownload.as_view()),]
		return urls

admin.site.register(JobApplication,JobApplicationAdmin)