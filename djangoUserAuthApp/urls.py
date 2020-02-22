from django.conf.urls import url
from djangoUserAuthApp import views

app_name = 'djangoUserAuthApp'

urlpatterns=[
    url(r'^register/$', views.register,name='register'),
    url(r'^user_login/$', views.user_login,name='user_login'),
]