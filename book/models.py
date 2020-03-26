from django.db import models

class BookInfo(models.Model):
    name = models.CharField(max_length=32, verbose_name='书名')
    pub_date = models.IntegerField(verbose_name='出版日期')
    bread = models.IntegerField(verbose_name='阅读量')
    bcomment = models.TextField(max_length=256, verbose_name='评论')

    class Meta:
        db_table = 'books'
        verbose_name = '书籍'
        verbose_name_plural = verbose_name

