from rest_framework.response import Response
from rest_framework.views import APIView
from book.serializers import BookInfoSerializer
from .models import BookInfo


class BookInfoView(APIView):
    def post(self, request):
        data = request.data
        serializer = BookInfoSerializer(data=data)
        if not serializer.is_valid():
            return Response({'msg': str(serializer.errors)})
        serializer.save()
        return Response({'msg': '输入正确', '输入信息为:': serializer.validated_data})



