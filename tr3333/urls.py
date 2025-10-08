from django.contrib import admin
from django.urls import path, include
from . import views  # استدعاء الملف views من المشروع الرئيسي

urlpatterns = [
    path('admin/', admin.site.urls),

    # الصفحة الرئيسية
    path('', views.home_view, name='home'),

    # تضمين مسارات التطبيقات الأخرى
    path('customers/', include('customers.urls')),
    path('catalog/', include('catalog.urls')),
    path('orders/', include('orders.urls')),
]

