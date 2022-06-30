from django.urls import path, include

from .views import SignInView, SignUpView, PersonalArea, logout_user

urlpatterns = [
   path('', include('django.contrib.auth.urls')),
   path('<int:pk>', PersonalArea.as_view(), name='personal_area'),
   path('sign_up/', SignUpView.as_view(), name='sign_up'),
   path('sign_in/', SignInView.as_view(), name='sign_in'),
   path('logout_user/', logout_user, name='logout_user'),
]