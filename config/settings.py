from pathlib import Path
import os
import dj_database_url
from datetime import timedelta

# ==========================================================

# BASE DIR

# ==========================================================

BASE_DIR = Path(**file**).resolve().parent.parent

# ==========================================================

# SECURITY CONFIG

# ==========================================================

SECRET_KEY = os.environ.get("SECRET_KEY", "fallback-secret-for-dev")
DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
"localhost",
"127.0.0.1",
"povabackend.onrender.com",  # Your Render backend URL
]

# ==========================================================

# INSTALLED APPS

# ==========================================================

INSTALLED_APPS = [
"django.contrib.admin",
"django.contrib.auth",
"django.contrib.contenttypes",
"django.contrib.sessions",
"django.contrib.messages",
"django.contrib.staticfiles",

```
# Third-party
"rest_framework",
"corsheaders",

# Your apps
"api",
```

]

# ==========================================================

# MIDDLEWARE

# ==========================================================

MIDDLEWARE = [
"corsheaders.middleware.CorsMiddleware",
"django.middleware.security.SecurityMiddleware",
"django.contrib.sessions.middleware.SessionMiddleware",
"django.middleware.common.CommonMiddleware",
"django.middleware.csrf.CsrfViewMiddleware",
"django.contrib.auth.middleware.AuthenticationMiddleware",
"django.contrib.messages.middleware.MessageMiddleware",
"django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

# ==========================================================

# TEMPLATES

# ==========================================================

TEMPLATES = [
{
"BACKEND": "django.template.backends.django.DjangoTemplates",
"DIRS": [BASE_DIR / "templates"],
"APP_DIRS": True,
"OPTIONS": {
"context_processors": [
"django.template.context_processors.debug",
"django.template.context_processors.request",
"django.contrib.auth.context_processors.auth",
"django.contrib.messages.context_processors.messages",
],
},
},
]

WSGI_APPLICATION = "config.wsgi.application"

# ==========================================================

# DATABASE

# ==========================================================

DATABASES = {
"default": dj_database_url.config(
default="sqlite:///" + str(BASE_DIR / "db.sqlite3"),
conn_max_age=600,
ssl_require=not DEBUG,
)
}

# ==========================================================

# AUTH PASSWORD VALIDATION

# ==========================================================

AUTH_PASSWORD_VALIDATORS = [
{"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
{"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
{"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
{"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ==========================================================

# INTERNATIONALIZATION

# ==========================================================

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ==========================================================

# STATIC & MEDIA

# ==========================================================

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ==========================================================

# CORS CONFIG

# ==========================================================

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
"[http://127.0.0.1:3000](http://127.0.0.1:3000)",
"http://localhost:3000",
"[https://povalogistics-com.vercel.app](https://povalogistics-com.vercel.app)",
"[https://trackingpage.vercel.app](https://trackingpage.vercel.app)",
]

CSRF_TRUSTED_ORIGINS = [
"[https://povabackend.onrender.com](https://povabackend.onrender.com)",
"[https://povalogistics-com.vercel.app](https://povalogistics-com.vercel.app)",
"[https://trackingpage.vercel.app](https://trackingpage.vercel.app)",
]

CORS_ALLOW_HEADERS = [
"accept",
"accept-encoding",
"authorization",
"content-type",
"origin",
"user-agent",
"dnt",
"connection",
"x-csrftoken",
"x-requested-with",
]

# ==========================================================

# REST FRAMEWORK

# ==========================================================

REST_FRAMEWORK = {
"DEFAULT_RENDERER_CLASSES": [
"rest_framework.renderers.JSONRenderer",
] if not DEBUG else [
"rest_framework.renderers.JSONRenderer",
"rest_framework.renderers.BrowsableAPIRenderer",
]
}

# ==========================================================

# DEFAULT AUTO FIELD

# ==========================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
