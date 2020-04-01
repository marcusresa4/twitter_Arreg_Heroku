from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from apps.oauth2 import views

urlpatterns = [
 	path('', views.index, name='index'),
 	path('', include('social_django.urls', namespace='social')),
 	path('', auth_views.LogoutView.as_view(next_page='/'), name='logout')
]