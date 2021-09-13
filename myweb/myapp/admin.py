from django.contrib import admin

# Register your models here.
from myapp.models import Stu

# admin.site.register(Stu)
@admin.register(Stu)
class StuAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段(id字段是Django模型的默认主键)
    list_display = ('id','name','sex','classid')
    list_display_links = ('id','name')
    list_per_page = 10
    ordering = ('id',)