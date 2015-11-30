#python imports

#django imports
from django.conf.urls import include, url
from django.contrib import admin

#local imports
from views import Home

#inter app imports

#third party imports

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',Home.as_view()),
    url(r'',include('job.urls')),
    url(r'',include('company.urls')),
]
