from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from book.models import BookInfo
from book.serializers import BookInfoSerializer
from student.models import Student
from .serializers import StudentModelSerialzer, StudentModel2Serializer
from rest_framework.response import Response

class StudentsGenericAPIView(GenericAPIView):
    queryset = Student.objects.all()

    serializer_class = StudentModelSerialzer

    def get(self, request):
        '''获取所有学生信息'''
        serializer = self.get_serializer(instance=self.get_queryset(), many=True)
        return Response(serializer.data)
    def post(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        serializer = self.get_serializer(instance=instance)
        return Response(serializer.data)

class StudentGenericAPIView(GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerialzer
    lookup_field = 'pk'

    def get_serializer_class(self):
        '''重写获取序列化器类的方法'''
        if self.request.method == 'GET':
            return StudentModel2Serializer
        else:
            return StudentModelSerialzer

    #在使用GenericAPIView视图获取操作单个数据的时候， 视图中发方法代表主键的参数最好是pk
    def get(self, request, pk):
        '''获取一条数据'''
        serializer = self.get_serializer(instance=self.get_object())
        return Response(serializer.data)
    def put(self, request, pk):
        data = request.data
        serializer = self.get_serializer(instance=self.get_object(), data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer = self.get_serializer(instance=self.get_object())
        return Response(serializer.data)



'''GenericAPIView结合视图扩展类实现api借口'''
class Students2GenericAPIView(GenericAPIView, ListModelMixin, CreateModelMixin):
    #本次视图类中要操作的数据{必填}
    queryset = Student.objects.all()
    #本次视图类中要使用的序列化器【必填】
    serializer_class = StudentModelSerialzer
    def get(self, request):
        '''获取多个学生'''
        return self.list(request)
    def post(self, request):
        '''添加学生信息'''
        return self.create(request)

from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
class Student2GenericAPIView(GenericAPIView,RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerialzer
    lookup_field = 'pk'

    #在使用GenericAPIView视图操作单个数据时，视图方法中的代表主键的参数最好时pk
    def get(self, request, pk):
        '''获取一条数据'''
        return self.retrieve(request, pk)
    def put(self, request, pk):
        '''更新一条数据'''
        return self.update(request, pk)
    def delete(self, request, pk):
        '''删除一条数据'''
        return self.destroy(request, pk)



from rest_framework.viewsets import ViewSet
class BookInfoViewSet(ViewSet):
    def list(self, request):
        books = BookInfo.objects.all()
        serializer = BookInfoSerializer(books, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            books = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookInfoSerializer(books)
        return Response(serializer.data)

































