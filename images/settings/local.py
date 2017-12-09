from .default import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$w@8tqm0vu5_u8^x6b@d5um9xg8=oy%u&e3t_i2&3@!rhjx%b!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'images',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
    }
}

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
