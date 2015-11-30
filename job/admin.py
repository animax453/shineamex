#python imports

#django imports
from django.contrib import admin

#local imports
from models import Job

#inter app imports

#third party imports

class JobAdmin(admin.ModelAdmin):
	exclude = ('edited_date',)

admin.site.register(Job,JobAdmin)