#python imports

#django imports
from django.conf.urls import include, url
from django.contrib import admin

#local imports

#inter app imports

#third party imports

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'',include('job.urls')),
    url(r'',include('company.urls')),
]
