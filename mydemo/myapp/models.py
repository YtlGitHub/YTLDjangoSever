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


class Family(models.Model):
    # id = models.AutoField(primary_key=True)  # 主键可省略不写
    name = models.CharField('姓名', max_length=32)
    age = models.IntegerField('年龄', default=20)
    sex = models.CharField('性别', max_length=32)
    address = models.CharField('地址', max_length=32)
    phone = models.CharField('电话号码', max_length=16)
    birthday = models.DateTimeField('生日', default=datetime.now)
    addTime = models.DateTimeField('添加时间', default=datetime.now)

    # def __str__(self):
    #     return f"{self.id,self.name,self.age,self.sex,self.address,self.phone,self.birthday,self.addTime}"

    class Meta:
        db_table = "family"  # 指定表名
        verbose_name_plural = '杨天龙家庭信息管理'
        verbose_name = '家庭信息数据'
