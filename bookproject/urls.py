from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from homeapp import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('game/',views.quizgame ,name='snakegame'),
    path('info/<int:book_id>/',views.bookdetails,name='bookdetails'),
     path('verify-email/', views.verify_email_view, name='verify_email'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/',auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('custom_logout/',views.custom_logout,name='custom_logout'),
    path('profile/edit/',views.edit_profile,name='edit_profile'),
    path('api/books/', views.get_books, name='get_books'),
     path('api/add-book/', views.AddBookAPIView.as_view(), name='add_book_api'),


    path('', views.Asosiypanel.as_view(), name='base'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
