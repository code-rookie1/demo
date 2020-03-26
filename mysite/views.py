import json
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models
from rest_framework import serializers

# class RolesSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField()
#
# class RolesView(APIView):
#     def get(self, request, *args, **kwargs):
#         roles = models.Role.objects.all().first()
#         ser = RolesSerializer(roles, many=False)
#         ret = json.dumps(ser.data, ensure_ascii=False)
#         return HttpResponse(ret)


#
# class UserInfoSerializer(serializers.Serializer):
#     '''序列化用户的信息'''
#     #user_type是choices（1,2,3），显示全称的方法用source
#     type = serializers.CharField(source="get_user_type_display")
#     username = serializers.CharField()
#     password = serializers.CharField()
#     #group.title：组的名字
#     group = serializers.CharField(source="group.title")
#     #SerializerMethodField(),表示自定义显示
#     #然后写一个自定义的方法
#     rls = serializers.SerializerMethodField()
#
#     def get_rls(self,row):
#         #获取用户所有的角色
#         role_obj_list = row.roles.all()
#         ret = []
#         #获取角色的id和名字
#         #以字典的键值对方式显示
#         for item in role_obj_list:
#             ret.append({"id":item.id,"title":item.title})
#         return ret
#
# class UserInfoView(APIView):
#     '''用户的信息'''
#     def get(self,request,*args,**kwargs):
#         users = models.UserInfo.objects.all()
#         ser = UserInfoSerializer(instance=users,many=True)
#         ret = json.dumps(ser.data,ensure_ascii=False)
#         return HttpResponse(ret)



# class UserInfoSerializer(serializers.ModelSerializer):
#     type = serializers.CharField(source="get_user_type_display")
#     group = serializers.CharField(source="group.title")
#     rls = serializers.SerializerMethodField()
#
#     def get_rls(self, row):
#         # 获取用户所有的角色
#         role_obj_list = row.roles.all()
#         ret = []
#         # 获取角色的id和名字
#         # 以字典的键值对方式显示
#         for item in role_obj_list:
#             ret.append({"id": item.id, "title": item.title})
#         return ret
#
#     class Meta:
#         model = models.UserInfo
#         fields = ['id','username','password','type','group','rls']
# from .serializers import UserInfoSerializer
from .serializers import UserInfoSerializer


class UserInfoView(APIView):
    '''用户的信息'''
    def get(self,request,*args,**kwargs):
        users = models.UserInfo.objects.all()
        ser = UserInfoSerializer(instance=users,many=True)
        print(ser.data)
        return Response(ser.data)