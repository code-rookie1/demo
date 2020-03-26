# from rest_framework import serializers,generics
#
from mysite import models
from mysite.models import UserInfo
#
#
# class UserInfoSerializers(serializers.ModelSerializer):
#     type = serializers.CharField(source='get_user_type_display')
#     group = serializers.CharField(source='group.title')
#     rls = serializers.SerializerMethodField()
#
#     def get_rls(self, row):
#         role_obj_list = row.roles.all()
#         ret = []
#         for item in role_obj_list:
#             ret.append({'id': item.id, 'title': item.title})
#         return ret
#
#     class Meta:
#         model = UserInfo,
#         fields = ['id', 'username', 'password', 'group', 'roles']
#         depth = 3
#
#
from rest_framework import serializers

from mysite.models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source="get_user_type_display")
    group = serializers.CharField(source="group.title")
    rls = serializers.SerializerMethodField()

    def get_rls(self, row):
        # 获取用户所有的角色
        role_obj_list = row.roles.all()
        ret = []
        # 获取角色的id和名字
        # 以字典的键值对方式显示
        for item in role_obj_list:
            ret.append({"id": item.id, "title": item.title})
        return ret

    class Meta:
        model = UserInfo
        fields = ['id','username','password','type','group','rls']