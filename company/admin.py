#python imports

#django imports
from django.contrib import admin

#local imports
from models import Company

#inter app imports

#third party imports

class CompanyAdmin(admin.ModelAdmin):
	exclude = ('created_date',)

admin.site.register(Company,CompanyAdmin)