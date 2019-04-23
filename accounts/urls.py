from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from . import views

app_name = 'accounts'
urlpatterns = [
    re_path('^', include('django.contrib.auth.urls')),
    re_path('^profile/$', views.redirect_to_user_profile, name='redirect-user-detail'),
    re_path('^profile/(?P<pk>\d+)/$', views.UserProfile.as_view(), name='user-detail'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]