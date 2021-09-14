# Generated by Django 3.2.6 on 2021-09-14 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='学号')),
                ('name', models.CharField(max_length=16, verbose_name='姓名')),
                ('age', models.SmallIntegerField(verbose_name='年龄')),
                ('sex', models.CharField(max_length=1, verbose_name='性别')),
                ('classid', models.CharField(max_length=8, verbose_name='班级')),
            ],
            options={
                'verbose_name': '浏览学生信息',
                'verbose_name_plural': '学生信息管理',
                'db_table': 'stu',
            },
        ),
    ]
