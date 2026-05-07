from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView

from accounting.views import company_home, health_check

urlpatterns = [
    path('', company_home, name='company-home'),
    path('index.html', RedirectView.as_view(pattern_name='company-home', permanent=False)),
    path('health/', health_check, name='health-check'),
    path('admin/', admin.site.urls),
    path('api/', include('accounting.urls')),
    re_path(r'^.*$', RedirectView.as_view(pattern_name='company-home', permanent=False)),
]
