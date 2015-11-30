#python imports

#django imports
from django.conf.urls import url

#local imports
from views import CompanyList

#inter app imports

#third party imports

urlpatterns = [
	url(r'^companies/$', CompanyList.as_view()),]