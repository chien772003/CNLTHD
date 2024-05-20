from django.core.validators import URLValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

class User(AbstractUser):
    id = models.AutoField(primary_key=True)  # Trường ID tự động tăng, làm khóa chính
    first_name = models.CharField(max_length=30)  # Tên (first name)
    last_name = models.CharField(max_length=30)  # Họ (last name)
    birth_year = models.PositiveIntegerField(null=True, blank=True)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

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
    url = models.URLField(max_length=200, blank=True, null=True, validators=[URLValidator()])
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
class Admin(User):
    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'

    def save(self, *args, **kwargs):
        self.is_admin = True
        super().save(*args, **kwargs)

class Student(User):

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def save(self, *args, **kwargs):
        self.is_student = True
        super().save(*args, **kwargs)

class Teacher(User):
    hocvi = models.CharField(max_length=50)
    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
        permissions = [
            ("can_change_teacher", "Can change teacher","can_change_Curriculum"),
        ]

    def save(self, *args, **kwargs):
        self.is_teacher = True
        super().save(*args, **kwargs)
