# Generated by Django 4.2.13 on 2024-06-15 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_alter_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluationcriterion',
            name='courses',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='syllabus/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='images/avatar/%Y/%m/%d/'),
        ),
    ]
