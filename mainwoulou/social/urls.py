from django.urls import URLPattern, path  , include
from django.urls import re_path
from .views  import FacebookLogin

urlpatterns = [
  
 re_path(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login')
]
#http://127.0.0.1:8000/social/rest-auth/facebook/