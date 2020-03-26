from django.db import models


class UserInfo(models.Model):
    USER_TYPE = (
        (1, '普通用户'),
        (2, 'VIP'),
        (3, 'SVIP'),
    )
    user_type = models.IntegerField(choices=USER_TYPE, verbose_name='用户类型')
    username = models.CharField(max_length=32, unique=True, verbose_name='用户名字')
    password = models.CharField(max_length=64, verbose_name='用户密码')
    group = models.ForeignKey('UserGroup', on_delete=models.CASCADE, verbose_name='用户组织')
    roles = models.ManyToManyField('Role', verbose_name='用户角色')

    class Meta:
        db_table = 'de_user'
        verbose_name = '用户信息表'
        verbose_name_plural = verbose_name


class UserToken(models.Model):
    user = models.OneToOneField('UserInfo', on_delete=models.CASCADE)
    token = models.CharField(max_length=64, verbose_name='用户令牌')

    class Meta:
        db_table = 'de_token'
        verbose_name = '令牌信息表'
        verbose_name_plural = verbose_name


class UserGroup(models.Model):
    title = models.CharField(max_length=32)

    class Meta:
        db_table = 'de_group'
        verbose_name = '组织信息表'
        verbose_name_plural = verbose_name


class Role(models.Model):
    title = models.CharField(max_length=32)

    class Meta:
        db_table = 'de_role'
        verbose_name = '用户角色'
        verbose_name_plural = verbose_name


























