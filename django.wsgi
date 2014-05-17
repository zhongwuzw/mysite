<span style="font-size: 14px;">#coding=utf-8
 
import os
import sys
import django.core.handlers.wsgi
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'appops.settings'
app_apth = "D:/OPSAPP/appops"
sys.path.append(app_apth)
application = django.core.handlers.wsgi.WSGIHandler()
</span>