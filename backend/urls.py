
from django.contrib import admin
from django.urls import path, include
from Dashboard.views import profile
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("allauth.urls")),
    path('accounts/profile/', profile, name='profile'),
]
