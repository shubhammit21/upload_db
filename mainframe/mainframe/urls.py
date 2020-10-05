from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
#    path(r'^$', views.home),
    path('', include('accounts.urls'))
]
