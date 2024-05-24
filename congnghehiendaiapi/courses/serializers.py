from rest_framework.serializers import ModelSerializer
from .models import Course

from rest_framework import serializers
from .models import User, Category, Course, Curriculum, Syllabus, EvaluationCriterion, Comment, Admin, Student, Teacher

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'birth_year', 'is_teacher', 'is_student', 'avatar', 'is_active', 'is_staff']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'credits', 'url', 'created_at', 'updated_at', 'active']

class CurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculum
        fields = ['id', 'course', 'teacher', 'title', 'description', 'start_year', 'end_year', 'created_at', 'updated_at', 'active']

class SyllabusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Syllabus
        fields = ['id', 'title', 'content', 'curriculums']

class EvaluationCriterionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluationCriterion
        fields = ['id', 'curriculum', 'name', 'weight', 'max_score', 'created_at', 'updated_at', 'active']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'curriculum', 'user', 'content', 'created_at', 'updated_at', 'active']

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'username', 'first_name', 'last_name', 'birth_year', 'is_teacher', 'is_student', 'avatar', 'is_active', 'is_staff']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'username', 'first_name', 'last_name', 'birth_year', 'is_teacher', 'is_student', 'avatar', 'is_active', 'is_staff']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'username', 'first_name', 'last_name', 'birth_year', 'is_teacher', 'is_student', 'avatar', 'is_active', 'is_staff', 'HocVi']
