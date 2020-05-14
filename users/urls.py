from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users import views

urlpatterns = [
    path(
        'auth/token/',
        views.EmailCodeTokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'auth/token/refresh',
        views.EmailCodeTokenObtainPairView.as_view(),
        name='token_refresh'
    ),
    path(
        'auth/email/',
        views.send_confirmation_code,
        name='send_confirmation_code'
    )
]

router = DefaultRouter()
router.register('users', views.UsersViewSet, basename='users')

urlpatterns += [
    path('', include(router.urls)),
]
