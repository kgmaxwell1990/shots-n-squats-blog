from django.conf.urls import url
from .views import logout, profile, login, register

urlpatterns = [
    url(r'^register', register, name='register'),
    url(r'^logout', logout, name='logout'),
    url(r'^login', login, name='login'),
    url(r'^profile', profile, name='profile'),

]