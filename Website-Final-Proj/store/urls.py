from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse
from appstore import views


urlpatterns = [
    path('admin/', admin.site.urls),


    path('', include('appstore.urls')),

]
