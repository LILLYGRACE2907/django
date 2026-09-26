from django.contrib import admin
from django.urls import path
from home.views import home,about,contact,services

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('about/', about),
    path('contact/', contact),
    path('services/', services),
] 