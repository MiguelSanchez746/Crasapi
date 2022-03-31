# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-vwub^*@v8ftj-348icj!py6_s&h!qqnq11onsg17*^@ao!5=5f'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER' : 'root' ,
        'PASSWORD' : '91_Bravo' 
    }
}