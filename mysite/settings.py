#coding=utf8
"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5hy_g$rk+fldv@#dcz5#m*-+k+zk=urwh8xj83^ym=fxo9(dj@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DIRS = (os.path.join(BASE_DIR,'templates'),)

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'books',
    'django.contrib.sites',
    'django.contrib.comments',
    'django.contrib.flatpages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',#Translate admin page to Chinese,zhongwu
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'root',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-cn'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'

#settings.py

#�ʼ�����
EMAIL_HOST = 'smtp.sina.com'                   #SMTP��ַ
EMAIL_PORT = 25                                 #SMTP�˿�
EMAIL_HOST_USER = 'zhongwuzw@sina.com'       #���Լ�������
EMAIL_HOST_PASSWORD = ''                  #�ҵ���������
EMAIL_SUBJECT_PREFIX = u'[����]'            #Ϊ�ʼ�Subject-lineǰ׺,Ĭ����'[django]'
EMAIL_USE_TLS = True                             #��SMTP������ͨ��ʱ���Ƿ�����TLS����(��ȫ����)��Ĭ����false
#����Ավ��
SERVER_EMAIL = 'zhongwuzw@qq.com'            #The email address that error messages come from, such as those sent to ADMINS and MANAGERS.
LOGIN_REDIRECT_URL = '/contactemail'   #edit defalut page for success login.zhongwu
SITE_ID = 1    #Add by myself.zhongwu
