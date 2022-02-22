from django.contrib import admin
from django.urls import path, include
from home import views 

# Django admin header customizaation 

admin.site.site_header = "Developer Portal"
admin.site.site_title = "Welcome To Dashboard"
admin.site.index_title = "Welcome To This Portal"








urlpatterns = [
    
    path('', views.home, name='home' ),
    path('about', views.about, name='about' ),
    path('project', views.project, name='project' ),
    path('contact', views.contact, name='contact' )

] 