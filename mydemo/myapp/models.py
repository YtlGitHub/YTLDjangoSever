from django.db import models
from datetime import datetime
# Create your models here.


class Users(models.Model):
    id = models.AutoField(primary_key=True)  # 主键可省略不写
    name = models.CharField('姓名', max_length=32)
    age = models.IntegerField('年龄', default=20)
    sex = models.CharField('性别', max_length=32)
    classid = models.CharField('班级', max_length=32)
    # phone = models.CharField(max_length=16)
    addtime = models.DateTimeField('添加时间', default=datetime.now)

    # def __str__(self):
    #     return "%d:%s:%d:%s:%s:"%(self.id,self.name,self.age,self.sex,self.classid)
    # def __str__(self):
    #     return f"{self.id,self.name,self.age,self.sex,self.classid,self.addtime}"

    class Meta:
        db_table = "stu"  # 指定表名
        verbose_name_plural = '信息库'
        verbose_name = '信息数据'
