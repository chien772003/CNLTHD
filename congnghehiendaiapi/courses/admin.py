from django.contrib import admin
from .models import Course, Comment, Curriculum,EvaluationCriterion


# Register your models here.


admin.site.register(Course)
admin.site.register(Comment)
admin.site.register(EvaluationCriterion)
admin.site.register(Curriculum)
