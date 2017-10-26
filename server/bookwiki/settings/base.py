import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nq72#e76c(jy$jh$%v^=3kr_+oq2=cq1ko+rh)s_#&qm(y6px+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap',
    'markdownx',
    'pipeline',
    'bookwiki',
    'bookwiki.core',
    'bookwiki.books',
    'bookwiki.projects',
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

ROOT_URLCONF = 'bookwiki.urls'
APPEND_SLASH = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'bookwiki.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'bookwiki.db'),
    }
}


# Authentication

AUTH_USER_MODEL = 'core.User'
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
STATIC_URL = '/static/'
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
]
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

PIPELINE = {
    'COMPILERS': ('pipeline.compilers.less.LessCompiler',),
    'LESS_BINARY': os.path.join('C:\\', 'Program Files', 'nodejs', 'node.exe') + ' ' + os.path.join('C:\\', 'Users', 'blackstone', 'AppData', 'Roaming', 'npm', 'node_modules', 'less', 'bin', 'lessc'),
    'STYLESHEETS': {
        'fonts': {
            'source_filenames': (
                'css/fonts.css',
            ),
            'output_filename': 'css/fonts.css',
        },
        'bookwiki': {
            'source_filenames': (
                'css/fonts.css',
                'markdownx/admin/css/markdownx.min.css',
                'css/style.css',
                'css/colors.less',
            ),
            'output_filename': 'css/compiled.css',
        },
    },
    'JAVASCRIPT': {
        'bookwiki': {
            'source_filenames': (
                'markdownx/js/markdownx.min.js',
            ),
            'output_filename': 'js/compiled.js',
        },
    }
}

# Book-wiki settings

REPOSITORY_ROOT = os.path.join(BASE_DIR, 'repo')

