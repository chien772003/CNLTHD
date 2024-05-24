from django.shortcuts import render
from rest_framework import viewsets, permissions, status, parsers, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import User, Category, Course, Curriculum, Syllabus, EvaluationCriterion, Comment, Admin, Student, Teacher
from .serializers import UserSerializer, CategorySerializer, CourseSerializer, CurriculumSerializer, SyllabusSerializer, EvaluationCriterionSerializer, CommentSerializer, AdminSerializer, StudentSerializer, TeacherSerializer
from courses import serializers, paginators

class UserViewSet(viewsets.ViewSet, generics.CreateAPIView, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [parsers.MultiPartParser]
    # permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer
    pagination_class = paginators.CoursePaginator

    def get_queryset(self):
        queryset = self.queryset
        q = self.request.query_params.get('q')
        if q:
            queryset = queryset.filter(name__icontains=q)
        cate_id = self.request.query_params.get('category_id')
        if cate_id:
            queryset = queryset.filter(category_id=cate_id)
        return queryset

    @action(methods=['get'], url_path='lessons', detail=True)
    def get_lessons(self, request, pk=None):
        course = self.get_object()
        lessons = course.lesson_set.filter(active=True)
        return Response(serializers.LessonSerializer(lessons, many=True).data, status=status.HTTP_200_OK)

class CurriculumViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer

class SyllabusViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Syllabus.objects.all()
    serializer_class = SyllabusSerializer

class EvaluationCriterionViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = EvaluationCriterion.objects.all()
    serializer_class = EvaluationCriterionSerializer

class CommentViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class AdminViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class StudentViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
