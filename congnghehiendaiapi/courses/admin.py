from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path
from django.contrib.auth.models import Permission, Group
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.admin import GroupAdmin
from .models import Course, Comment, Curriculum, EvaluationCriterion, User, Category, Syllabus
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'birth_year', 'is_teacher', 'is_student', 'avatar', 'HocVi')

class CustomUserAdmin(DefaultUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    fieldsets = DefaultUserAdmin.fieldsets + (
        (None, {'fields': ('birth_year', 'is_teacher', 'is_student', 'avatar', 'HocVi')}),
    )

    add_fieldsets = DefaultUserAdmin.add_fieldsets + (
        (None, {'fields': ('birth_year', 'is_teacher', 'is_student', 'avatar', 'HocVi')}),
    )

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

admin_site = CourseAppAdminSite(name='Hệ thống quản lý đề cương')

# Register your models here.
admin_site.register(User, CustomUserAdmin)
admin_site.register(Category)
admin_site.register(Course)
admin_site.register(Curriculum)
admin_site.register(Syllabus)
admin_site.register(EvaluationCriterion)
admin_site.register(Comment)
admin_site.register(Group, GroupAdmin)
admin_site.register(Permission)
