from rest_framework import serializers
from student.models import Student

class StudentModelSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class StudentModel2Serializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'class_null']