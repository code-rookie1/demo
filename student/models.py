from django.db import models

class Student(models.Model):
    # 模型字段
    name = models.CharField(max_length=100,verbose_name="姓名",help_text="提示文本:账号不能为空！")
    sex = models.BooleanField(default=True,verbose_name="性别")
    age = models.IntegerField(verbose_name="年龄")
    class_null = models.CharField(max_length=5,verbose_name="班级编号")
    description = models.TextField(verbose_name="个性签名")

    class Meta:
        db_table="tb_student"
        verbose_name = "学生"
        verbose_name_plural = verbose_name