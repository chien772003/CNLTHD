# Generated by Django 4.2.13 on 2024-06-12 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='syllabus',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='static/syllabus'),
        ),
    ]
