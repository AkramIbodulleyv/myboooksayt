from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from homeapp import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('game/',views.snakegame,name='snakegame'),
    path('base/',views.Asosiypanel.as_view(),name='base'),
    path('info/<int:book_id>/',views.bookdetails,name='bookdetails'),
     path('verify-email/', views.verify_email_view, name='verify_email'),
    path('add/',views.addbook,name='addbook'),
    path('login/', views.login_view, name='login'),
    path('', views.signup_view, name='signup'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
