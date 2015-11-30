#python imports

#django imports
from django.conf.urls import url

#local imports
from views import JobList

#inter app imports

#third party imports

urlpatterns = [
	url(r'^jobs/$', JobList.as_view()),
    url(r'^jobs/(?P<company_name>[a-z0-9 -]+)/(?P<company_id>[a-z0-9 -]+)/$', JobList.as_view()),]