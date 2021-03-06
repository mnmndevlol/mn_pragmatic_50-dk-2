from .base import *

# def read_secret(secret_name):
#     file = open('/run/secrets/' + secret_name)
#     secret = file.read()
#     secret = secret.rstrip().lstrip()
#     file.close()
#     return secret

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file

environ.Env.read_env(str(BASE_DIR.joinpath('.env')))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = read_secret('DJANGO_SECRET_KEY')
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'roqkf1234',
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}