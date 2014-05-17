from django.conf.urls import patterns, include, url
from mysite.views import hello,default_page,current_datetime,hours_ahead
from django.contrib import admin
from books.views import search_form,search,congratulations,contact,contactemail
from django.contrib.auth.views import login,logout
from django.http import HttpResponseRedirect
admin.autodiscover()

#login_info = {
      #        'extra_context':{'next':'/contactemail',}
       #       }

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    ('^hello/$',hello),
    ('^$',default_page),
    ('^time/$',current_datetime),
    (r'^time/plus/(\d{1,2})/$',hours_ahead),
    url(r'^admin/', include(admin.site.urls)),
    (r'^search-form/$',search_form),
    (r'^search/$',search),
    (r'^contact/thanks/$',congratulations),
    (r'^contact/$',contact),
    (r'^contactemail/$',contactemail),
    (r'^hello_pdf/$','books.views.hello_pdf'),
    (r'^accounts/login/$',login),
    (r'^accounts/logout/$',logout),
    (r'^register/$','books.views.register'),
    (r'^message/test/$','books.views.message_test'),
)
