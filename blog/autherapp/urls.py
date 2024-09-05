from django.urls import path

from .views import AutherUpdate, AutherView

urlpatterns = [
    path("auther/", AutherView.as_view(), name="auther"),
    path("auther/<int:i>/", AutherUpdate.as_view(), name="update"),
]
