from rest_framework import serializers

from case01.models import ClassRoom, Student, Teacher

class StudentSer(serializers.ModelSerializer):
    class Meta:
        model = Student