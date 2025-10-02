from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # روابط التطبيقات
    path('catalog/', include('catalog.urls')),      # روابط تطبيق المنتجات
    path('orders/', include('orders.urls')),        # روابط تطبيق الطلبات
    path('customers/', include('customers.urls')),  # روابط تطبيق العملاء
]
