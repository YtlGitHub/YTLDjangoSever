from django.contrib import admin
from myapp.models import Users,Family
# Register your models here.


# admin.site.register(Users)


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'sex', 'classid', 'addtime')
    list_display_links = ('id', 'name', )
    list_per_page = 10
    ordering = ('id', )
    list_editable = ['classid', ]


@admin.register(Family)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'sex', 'address', 'phone', 'birthday', 'addTime')
    list_display_links = ('id', 'name', )
    list_per_page = 10
    ordering = ('id', )
    # list_editable = ['birthday', ]
