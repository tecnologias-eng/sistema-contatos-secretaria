DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'contatos',
        'USER': 'postgres',
        'PASSWORD': 'Ceuazul.10',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'contatos',  # <-- Adicione esta linha
]
