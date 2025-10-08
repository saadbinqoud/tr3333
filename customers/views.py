from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.db import IntegrityError

# إنشاء حساب
def register_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.create_user(username=email, email=email, password=password, first_name=name)
            user.save()
            messages.success(request, "تم إنشاء الحساب بنجاح، يمكنك تسجيل الدخول الآن.")
            return redirect("login")
        except IntegrityError:
            messages.error(request, "البريد الإلكتروني مسجل مسبقاً.")
        except Exception as e:
            messages.error(request, f"حدث خطأ: {e}")

    return render(request, "customers_tamplate/register.html")


# تسجيل الدخول
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, f"مرحباً {user.first_name}!")
            return redirect("home")  # يمكنك تغييره إلى الصفحة التي تريدها بعد الدخول
        else:
            messages.error(request, "بيانات الدخول غير صحيحة.")

    return render(request, "customers_tamplate/login.html")
