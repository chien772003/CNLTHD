from django.contrib import admin
from django.urls import path, include
from . import views
from .admin import admin_site
from rest_framework import routers
from .views import UserViewSet, CategoryViewSet, CourseViewSet, CurriculumViewSet, SyllabusViewSet, EvaluationCriterionViewSet, CommentViewSet, AdminViewSet, StudentViewSet, TeacherViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'curriculums', CurriculumViewSet)
router.register(r'syllabuses', SyllabusViewSet)
router.register(r'evaluation-criteria', EvaluationCriterionViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'admins', AdminViewSet)
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)

urlpatterns = [
    # path('', views.index, name="index"),
    path('admin/', admin_site.urls),
    path('', include(router.urls))
]
