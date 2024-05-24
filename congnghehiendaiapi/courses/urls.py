from django.contrib import admin
from django.urls import path, include
from . import views
from .admin import admin_site
from rest_framework import routers
from .views import UserViewSet, CategoryViewSet, CourseViewSet, CurriculumViewSet, SyllabusViewSet, EvaluationCriterionViewSet, CommentViewSet, AdminViewSet, StudentViewSet, TeacherViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'curriculums', CurriculumViewSet, basename='curriculum')
router.register(r'syllabuses', SyllabusViewSet, basename='syllabus')
router.register(r'evaluationcriteria', EvaluationCriterionViewSet, basename='evaluationcriterion')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'admins', AdminViewSet, basename='admin')
router.register(r'students', StudentViewSet, basename='student')
router.register(r'teachers', TeacherViewSet, basename='teacher')

urlpatterns = [
    # path('', views.index, name="index"),
    path('admin/', admin_site.urls),
    path('', include(router.urls))
]
