#python imports

#django imports
from django.views.generic import ListView

#local imports
from models import Company

#inter app imports

#third party imports

class CompanyList(ListView):

	paginate_by = 10
	template_name = 'company_list.html'
	queryset = Company.objects.all().order_by('-created_date')
