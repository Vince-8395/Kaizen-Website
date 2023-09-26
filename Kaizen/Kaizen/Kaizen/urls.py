from django.contrib import admin
from django.urls import path, include
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'Kaizen_Project/', include('Kaizen_Project.urls')), 
    path(r'registration/', views.registration),
    path(r'about/', views.about),
    path(r'', views.homepage)
]

urlpatterns += staticfiles_urlpatterns()