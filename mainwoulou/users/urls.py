from django.urls import path  , include
from .views import MyObtainTokenPairView , RegisterView #, UserAPIView
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import re_path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', RegisterView)



urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   # re_path('register/', RegisterView.as_view(), name='auth_register'),
    path('api/', include(router.urls)),

]