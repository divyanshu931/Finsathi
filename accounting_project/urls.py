from django.contrib import admin
from django.urls import include, path

from accounting.views import company_home

urlpatterns = [
    path('', company_home, name='company-home'),
    path('admin/', admin.site.urls),
    path('api/', include('accounting.urls')),
]
