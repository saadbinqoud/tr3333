from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.html import format_html

# ==============================
# 🏷️ نموذج الأقسام
# ==============================
class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="اسم القسم"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="الوصف"
    )

    class Meta:
        verbose_name = "قسم"
        verbose_name_plural = "الأقسام"

    def __str__(self):
        return self.name


# ==============================
# 🛍️ نموذج المنتجات
# ==============================
class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="القسم"
    )
    name = models.CharField(
        max_length=200,
        verbose_name="اسم المنتج"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="الوصف"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="السعر"
    )
    stock = models.PositiveIntegerField(
        default=0,
        verbose_name="المخزون"
    )

    # ✅ الحقل الصحيح لرفع الصور إلى Cloudinary مباشرة
    image = CloudinaryField(
        verbose_name="صورة المنتج",
        null=True,
        blank=True,
        overwrite=True,       # في حال رفع صورة بنفس الاسم يتم استبدالها
        resource_type="image" # يضمن أن الملف صورة
    )

    is_available = models.BooleanField(
        default=True,
        verbose_name="متوفر للبيع"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإضافة"
    )

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    # ✅ عرض الصورة في لوحة التحكم بشكل مصغّر
    def image_preview(self):
        if self.image:
            try:
                return format_html(
                    f'<img src="{self.image.url}" width="80" height="80" '
                    f'style="border-radius:8px; object-fit:cover;">'
                )
            except Exception:
                return "⚠️ لا يمكن عرض الصورة"
        return "—"

    image_preview.short_description = "معاينة الصورة"
