#python imports

#django imports
from django.conf.urls import url

#local imports
from views import JobList, JobDetail, JobApplicationView, ThanksView

#inter app imports

#third party imports

urlpatterns = [
	url(r'^jobs/$', JobList.as_view()),
    url(r'^jobs/(?P<company_name>[a-z0-9 -]+)/(?P<company_id>[a-z0-9 -]+)/$', JobList.as_view()),
    url(r'^job/(?P<job_title>[a-z0-9 -]+)/(?P<job_id>[0-9]+)/$', JobDetail.as_view()),
    url(r'^apply/(?P<job_id>[0-9]+)/$', JobApplicationView.as_view()),
    url(r'^thanks/$', ThanksView.as_view()),]