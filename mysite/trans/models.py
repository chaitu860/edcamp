from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Course(models.Model):
    course_id=models.CharField(max_length=100,primary_key=True)
    instructor=models.ForeignKey(User, on_delete=models.CASCADE)

    domain=models.CharField(max_length=200)
    
class EnrolledList(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    course_info=models.ForeignKey(Course, on_delete=models.CASCADE)
class Video(models.Model):
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    video_id=models.IntegerField(primary_key=True)
    thumb_nail=models.FileField(upload_to='static/')
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    video=models.FileField(upload_to='static/')


