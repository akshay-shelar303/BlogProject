from django.contrib import admin
from django.urls import include, path

from Accounts.views import create_user

# from rest_framework.routers import DefaultRouter
# from blogapp.views import BlogViewSet


# router = DefaultRouter()
# router.register('blog', BlogViewSet, basename='blog')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blogapp.urls")),
    path("", include("autherapp.urls")),
    path("create_user/", create_user),
    # path("create_token/", create_user_token),
    # path('', include(router.urls)),
]
