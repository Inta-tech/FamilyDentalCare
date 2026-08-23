"""Django settings for config project."""

import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Security & Environment Settings
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "django-insecure-r&sgnq_4(ngaza0@7i)p7tefih&&wsy+59d+ap7$d^dx3u4yc$",
)

# False in production, controlled via Environment Variable
DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "cloudinary_storage",  # Must be placed above staticfiles
    "django.contrib.staticfiles",
    "cloudinary",
    # Family Dental Care apps
    "accounts",
    "clinic",
    "appointments",
    "content",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Serves CSS/JS on Render
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL:
    db_config = dj_database_url.parse(DATABASE_URL, conn_max_age=600)
    if "OPTIONS" in db_config:
        db_config["OPTIONS"].pop("ssl-mode", None)
        db_config["OPTIONS"].pop("ssl_mode", None)
    db_config["OPTIONS"] = db_config.get("OPTIONS", {})
    db_config["OPTIONS"]["ssl"] = {"ssl": True}
else:
    db_config = dj_database_url.config(
        default=f"mysql://root:{os.getenv('DB_PASSWORD', 'haaa@#$%^')}@127.0.0.1:3306/family_dental_care",
        conn_max_age=600,
    )

DATABASES = {"default": db_config}


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]


# Cloudinary Storage Configuration
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.getenv("CLOUDINARY_CLOUD_NAME"),
    "API_KEY": os.getenv("CLOUDINARY_API_KEY"),
    "API_SECRET": os.getenv("CLOUDINARY_API_SECRET"),
}

# Modern Django 5.x Storage Configuration
STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

# Legacy fallback for django-cloudinary-storage
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

# Prevent WhiteNoise from crashing during collectstatic on missing internal admin files
WHITENOISE_USE_FINDERS = True
WHITENOISE_MANIFEST_STRICT = False

# Real Email Configuration (Gmail SMTP)
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = f"Family Dental Care <{os.getenv('EMAIL_HOST_USER')}>"