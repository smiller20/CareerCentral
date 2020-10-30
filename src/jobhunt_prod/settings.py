"""
Django settings for jobhunt_prod project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/


login issue..gmail less ecure apps 

https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/
#STATIC_DIR = os.path.join(BASE_DIR,'static/')
#STATICFILES_DIRS =[ os.path.join(BASE_DIR, 'static/')]
#print(STATICFILES_DIRS)

"""
import os 

from pathlib import Path
import dj_database_url

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # During development only

EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
is_prod = os.environ.get('IS_HEROKU', None)

if not is_prod:
    from . import conf
    EMAIL_HOST = conf.email_host
    EMAIL_PORT = conf.email_port
    EMAIL_HOST_USER = conf.email_user
    EMAIL_HOST_PASSWORD = conf.email_password
    EMAIL_USE_TLS = True
    EMAIL_USE_SSL = False
    
    SECRET_KEY = conf.app_key
    DATABASES = {
        'default': {
            'ENGINE':conf.engine, 
            'HOST': conf.host, 
            'NAME': conf.name,
            'USER':conf.user,
            'PORT':conf.port,
            'PASSWORD':conf.password,
            'database':conf.db
            
            
        }
    }
else:


    EMAIL_HOST = os.environ.get('email_host', None)
    EMAIL_PORT = os.environ.get('email_port', None)
    EMAIL_HOST_USER = os.environ.get('email_user', None)
    EMAIL_HOST_PASSWORD =os.environ.get('email_password', None)
    EMAIL_USE_TLS = True
    EMAIL_USE_SSL = False

    SECRET_KEY = os.environ.get('APP_KEY', None)
    DATABASES = {
        'default': {
            'ENGINE':os.environ.get('engine', None), 
            'HOST': os.environ.get('host', None), 
            'NAME': os.environ.get('name', None),
            'USER':os.environ.get('user', None),
            'PORT':os.environ.get('port', None),
            'PASSWORD':os.environ.get('password', None),
            'database':os.environ.get('database', None)
            
            
        }
    }


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
print('base directory: ', BASE_DIR)




DEBUG = True

ALLOWED_HOSTS = ['careercentral.herokuapp.com', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'jobhunt_prod.apps.JobHuntConfig', 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'jobhunt_prod.urls'
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates/')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'jobhunt_prod.wsgi.application'




# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },

    {
        'NAME' : 'django.contrib.auth.password_validation.SpecialCharacterValidator',
    }

]



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/collect/')


STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'static/'),
)

