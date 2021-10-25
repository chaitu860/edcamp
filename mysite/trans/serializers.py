from rest_framework import serializers
from django.contrib.auth.models import User
from .models import EnrolledList,Course,Video

class userlistSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email']
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=['course_id','domain','name']
class EnrolledListSerializer(serializers.ModelSerializer):
    class Meta:
        model=EnrolledList
        fields="__all__"
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Video
        fields="__all__"
    
