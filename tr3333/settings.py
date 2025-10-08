from pathlib import Path
import os
import cloudinary
from cloudinary.api import ping
from decouple import config

# ==============================
#   🏗️ المسار الرئيسي للمشروع
# ==============================
BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================
#   🔑 إعدادات الأمان
# ==============================
SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", default=True, cast=bool)
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="").split(",")

# ==============================
#   🧩 التطبيقات المثبتة
# ==============================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # مكتبات خارجية
    'cloudinary',
    'cloudinary_storage',

    # تطبيقات المشروع
    'catalog',
    'customers',
    'orders',
]

# ==============================
#   ⚙️ الـ Middleware
# ==============================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ==============================
#   🔗 روابط المشروع
# ==============================
ROOT_URLCONF = 'tr3333.urls'

# ==============================
#   🧱 إعدادات القوالب
# ==============================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates",
            BASE_DIR / "templates" / "catalog_tamplate",
            BASE_DIR / "templates" / "customers_tamplate",
            BASE_DIR / "templates" / "orders_tamplate",
        ],
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

# ==============================
#   🚀 WSGI
# ==============================
WSGI_APPLICATION = 'tr3333.wsgi.application'

# ==============================
#   🗄️ إعدادات قاعدة البيانات
# ==============================
ENVIRONMENT = config("ENVIRONMENT", default="development")

if ENVIRONMENT == "production":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config("DB_NAME"),
            'USER': config("DB_USER"),
            'PASSWORD': config("DB_PASSWORD"),
            'HOST': config("DB_HOST"),
            'PORT': config("DB_PORT"),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# ==============================
#   🔐 التحقق من كلمات المرور
# ==============================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ==============================
#   🌍 اللغة والمنطقة الزمنية
# ==============================
LANGUAGE_CODE = config("LANGUAGE_CODE", default="ar")
TIME_ZONE = config("TIME_ZONE", default="Asia/Riyadh")
USE_I18N = True
USE_TZ = True

# ==============================
#   📦 الملفات الثابتة
# ==============================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# ==============================
#   ☁️ إعدادات Cloudinary
# ==============================
CLOUDINARY_CLOUD_NAME = config("CLOUDINARY_CLOUD_NAME")
CLOUDINARY_API_KEY = config("CLOUDINARY_API_KEY")
CLOUDINARY_API_SECRET = config("CLOUDINARY_API_SECRET")

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": CLOUDINARY_CLOUD_NAME,
    "API_KEY": CLOUDINARY_API_KEY,
    "API_SECRET": CLOUDINARY_API_SECRET,
}

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

cloudinary.config(
    cloud_name=CLOUDINARY_CLOUD_NAME,
    api_key=CLOUDINARY_API_KEY,
    api_secret=CLOUDINARY_API_SECRET,
    secure=True,
)

# ✅ اختبار الاتصال في وضع التطوير فقط
if DEBUG:
    try:
        status = ping()
        print(f"✅ Cloudinary Ping: {status}")
    except Exception as e:
        print(f"❌ فشل الاتصال بـ Cloudinary: {e}")

# ==============================
#   📂 ملفات الميديا
# ==============================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# ==============================
#   ⚙️ الإعداد الافتراضي للمفاتيح
# ==============================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
