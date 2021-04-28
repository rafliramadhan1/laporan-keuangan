from django.urls import path
from apps.accounts.views import RegisterUser
from rest_framework_simplejwt import views as jwt_views

app_name = "accounts"

urlpatterns = [
    path('registeruser/', RegisterUser.as_view(), name='registeruser'),
    path('usertoken/', jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('usertoken/refresh/', jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
]
