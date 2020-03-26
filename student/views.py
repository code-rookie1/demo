from django.views import View
from student.models import Student
from .serializers import StudentSerializer
from django.http.response import JsonResponse

class StudentView(View):
    """使用序列化器序列化转换单个模型数据"""
    def get(self, request):
        # 获取数据
        student = Student.objects.get(pk=1)
        # 数据转换[序列化过程]
        serializer = StudentSerializer(instance=student)
        print(serializer.data)
        # 响应数据
        return JsonResponse(serializer.data)