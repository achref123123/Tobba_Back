from django.urls import path
from .views import PatientRegistrationAPIView, UserLoginAPIView, UserTokenAPIView,DoctorRegistrationAPIView,ProfileViewSet

app_name = 'users'

urlpatterns = [
    path('patient/', PatientRegistrationAPIView.as_view(), name="list"),
    path('doctor/', DoctorRegistrationAPIView.as_view(), name="list"),
    path('profile/',ProfileViewSet.as_view(), name="list"),
    path('users/login/', UserLoginAPIView.as_view(), name="login"),
    path('tokens/<key>/', UserTokenAPIView.as_view(), name="token"),
]
