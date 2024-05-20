from django.contrib import admin
from django.urls import path, include
from . import views
from .admin import admin_site
from rest_framework import routers

router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet)
urlpatterns = [
    # path('', views.index, name="index"),
    path('admin/', admin_site.urls),
    path('', include(router.urls))
]
