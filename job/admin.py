#python imports

#django imports
from django.contrib import admin

#local imports
from models import Job, JobApplication

#inter app imports

#third party imports

class JobAdmin(admin.ModelAdmin):
	exclude = ('edited_date',)

admin.site.register(Job,JobAdmin)

class JobApplicationAdmin(admin.ModelAdmin):
	pass

admin.site.register(JobApplication,JobApplicationAdmin)