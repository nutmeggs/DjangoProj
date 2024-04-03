import re
from django.contrib import admin
from django.urls import path
from django.urls import include, re_path
import MyApp1.views
from MyApp1.views import studenthome

/*initializes a list that will hold all the URL patterns for the application.*/
urlpatterns = [
//Django will direct them to the admin interface if the url pattern has admin/
    path('admin/', admin.site.urls),
// When using a root URL Django will call the index function in the views.py file of the MyApp1 application.
    re_path(r'^$', MyApp1.views.index, name = 'index'),
//same thing here but if it has home/ will still call the index function
    re_path(r'^home$', MyApp1.views.index, name = 'home'),

//new url called studenthome/ that redirects to the students home page
    path('studenthome/', studenthome, name='student_home'),
]
