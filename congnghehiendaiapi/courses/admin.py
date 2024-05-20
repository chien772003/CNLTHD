from django.contrib import admin
from django.template.response import TemplateResponse

from .models import Course, Comment, Curriculum, EvaluationCriterion, Student, Teacher
from django.urls import path

class LessonAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "created_date", "active", "courses "]
    search_fields = []
    list_filter = []


class CourseAppAdminSite(admin.AdminSite):
    site_header = 'Hệ thống quản lý đề cương'
    def get_urls(self):
        return [
            path('course-stats/', self.course_stats)
        ] + super().get_urls()
    def course_stats(self, request):
        courses_count = Course.objects.count()
        # stats = Course.objects.annotate()
        return TemplateResponse(request, 'admin/courses_stats.html',{
            'courses_count': courses_count
        })

admin_site = CourseAppAdminSite(name='myadmin')
# Register your models here.
admin_site.register(Course)
admin_site.register(Comment)
admin_site.register(EvaluationCriterion)
admin_site.register(Curriculum)
admin_site.register(Teacher)
admin_site.register(Student)
