from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username

class BaseModel(models.Model):
    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Course(BaseModel):
    name = models.CharField(max_length=255)
    credits = models.PositiveIntegerField()

    def __str__(self):
        return self.name
class Curriculum(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class EvaluationCriterion(BaseModel):
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    max_score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class Comment(BaseModel):
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'{self.user.username} - {self.curriculum.title}'

