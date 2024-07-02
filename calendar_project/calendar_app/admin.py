from django.contrib import admin
from .models import Task1,Task2,Task3,UserProfile
from django.template.response import TemplateResponse

class MyModelAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list.html'

class MemberAdmin(admin.ModelAdmin):
    list_display = ("user","date","time","title","description","approved",)
    list_filter = ["approved"]
    
admin.site.register(Task1,MemberAdmin)
admin.site.register(Task2,MemberAdmin)
admin.site.register(Task3,MemberAdmin)
admin.site.register(UserProfile)


#admin.site.register(Task1, MyModelAdmin)

