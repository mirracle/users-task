from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserGetAndCreateView, DigitsFromHashView, UserShortInfoView, UserListView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('user/', UserGetAndCreateView.as_view(), name='user_get_create_api'),
    path('user/hash/', DigitsFromHashView.as_view(), name='digit_from_hash_api'),
    path('user/info/short/', UserShortInfoView.as_view(), name='short_info_api'),
    path('user/list/', UserListView.as_view(), name='user_list'),
]
