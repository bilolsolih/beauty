from django.urls import path

from . import api_endpoints as views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.UserRegisterAPIView.as_view(), name='register'),
    path('login/', views.UserLoginAPIView.as_view(), name='login'),
    path('logout/', views.UserLogoutAPIView.as_view(), name='logout'),
    path('retrieve/', views.UserRetrieveAPIView.as_view(), name='retrieve'),
    path('update/', views.UserUpdateAPIView.as_view(), name='update'),
    path('delete/', views.UserDeleteAPIView.as_view(), name='delete')
]
