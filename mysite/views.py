from django.http import HttpResponse,Http404
from django.template.loader import get_template
from django.template import Context
import os
import datetime

def hello(request):
    return HttpResponse("Hello World")

def default_page(request):
    return HttpResponse("Home Page")

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date':now}))
    return HttpResponse(html)

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()  
    dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
    html = "<http><body>In %s hour(s), it will be %s.</body></html>" %(offset,dt)
  #  assert False
    return HttpResponse(html)
     
