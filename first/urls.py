
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('myapp.urls')),
    path('login', include('myapp.urls')),
    path('myapp', include('myapp.urls')),
    path('admin/', admin.site.urls),
    path('logout', include('myapp.urls')),
    path('reset_pass', include('myapp.urls'))

]
