import re
from django.contrib import admin
from django.urls import path
from django.urls import include, re_path
import MyApp1.views
from MyApp1.views import studenthome

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', MyApp1.views.index, name = 'index'),
    re_path(r'^home$', MyApp1.views.index, name = 'home'),

    path('studenthome/', studenthome, name='student_home'),
]
