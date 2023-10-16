from django.contrib import admin
from django.urls import path, include
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'Kaizen_Project/', include('Kaizen_Project.urls')), 
    path(r'Login/',views.Login),
    path(r'Registration/', views.Register),
    path(r'About/', views.About),
    path(r'LandingPage/', views.LandingPage),
     path(r'', views.Homepage)
]

urlpatterns += staticfiles_urlpatterns()