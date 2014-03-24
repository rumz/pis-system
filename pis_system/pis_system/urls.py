from billing.views import *
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',

    url(r'^billing$', billing),
    url(r'^billing/searchstudent?', search_student),
    url(r'^billing/getbill?', get_bill),
    url(r'^billing/getstudent?', get_student),
    url(r'^admin/', include(admin.site.urls)),
)
