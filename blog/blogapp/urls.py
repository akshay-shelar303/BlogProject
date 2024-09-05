from django.urls import path

from .views import blogview

urlpatterns = [path("blog/", blogview, name="blog")]
