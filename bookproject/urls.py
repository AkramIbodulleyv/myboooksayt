"""
URL configuration for bookproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from homeapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addbook/',views.addbook, name='addbook'),
    path('deletebook/<int:book_id>/', views.deletebook, name='deletebook'),
    path('book/<int:book_id>/edit/', views.editbook, name='editbook'),
    path('bookview/',views.viewaddbook, name='viewaddbook'),
    path('book/<int:book_id>/details/', views.book_details, name='book_details'),
    path('sotish/<int:pk>', views.sotish_form, name='sotish_form'),
    path('arizalar/',views.ariza, name='arizalar'),
    path('login/', views.login_view, name='login'),
    path('', views.signup_view, name='signup'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
