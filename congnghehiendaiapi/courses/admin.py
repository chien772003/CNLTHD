from django.contrib import admin
from .models import Course, Comment, Curriculum,EvaluationCriterion,Student, Teacher

class LessonAdmin(admin.ModelAdmin):
    list_display = ["id","name","created_date","active","courses "]
    search_fields = []
    list_filter = []

# Register your models here.
admin.site.register(Course)
admin.site.register(Comment)
admin.site.register(EvaluationCriterion)
admin.site.register(Curriculum)
admin.site.register(Teacher)
admin.site.register(Student)
