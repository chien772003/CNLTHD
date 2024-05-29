from django.shortcuts import render
from rest_framework import viewsets, permissions, status, parsers, generics,filters
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import User, Category, Course, Curriculum, Syllabus, EvaluationCriterion, Comment
from .serializers import UserSerializer, CategorySerializer, CourseSerializer, CurriculumSerializer, SyllabusSerializer, \
    EvaluationCriterionSerializer, CommentSerializer, CurriculumEvaluation, CurriculumEvaluationSerializer
from courses import serializers, paginators


class UserViewSet(viewsets.ViewSet, generics.CreateAPIView, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [parsers.MultiPartParser]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        user = serializer.save()
        if user.is_teacher:
            user.is_active = False
            user.save()


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView):
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


class CurriculumViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView, generics.CreateAPIView, generics.UpdateAPIView):
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer


class SyllabusViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView, generics.CreateAPIView, generics.UpdateAPIView):
    queryset = Syllabus.objects.all()
    serializer_class = SyllabusSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'curriculums__course__name', 'curriculums__course__credits', 'curriculums__user__username', 'curriculums__start_year', 'curriculums__end_year']

    def get_queryset(self):
        queryset = Syllabus.objects.all()
        title = self.request.query_params.get('title', None)
        course_name = self.request.query_params.get('course_name', None)
        course_credits = self.request.query_params.get('course_credits', None)
        user_username = self.request.query_params.get('user_username', None)
        start_year = self.request.query_params.get('start_year', None)
        end_year = self.request.query_params.get('end_year', None)

        if title:
            queryset = queryset.filter(title__icontains=title)
        if course_name:
            queryset = queryset.filter(curriculums__course__name__icontains=course_name)
        if course_credits:
            queryset = queryset.filter(curriculums__course__credits=course_credits)
        if user_username:
            queryset = queryset.filter(curriculums__user__username__icontains=user_username)
        if start_year:
            queryset = queryset.filter(curriculums__start_year=start_year)
        if end_year:
            queryset = queryset.filter(curriculums__end_year=end_year)

        return queryset


class EvaluationCriterionViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView, generics.CreateAPIView, generics.UpdateAPIView):
    queryset = EvaluationCriterion.objects.all()
    serializer_class = EvaluationCriterionSerializer

class CurriculumEvaluationViewSet(viewsets.ViewSet, generics.ListCreateAPIView, generics.RetrieveAPIView):
    queryset = CurriculumEvaluation.objects.all()
    serializer_class = CurriculumEvaluationSerializer

class CommentViewSet(viewsets.ViewSet, generics.ListAPIView, generics.DestroyAPIView, generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
