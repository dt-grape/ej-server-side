from django.contrib import admin
# Register your models here.

from .models import Mark, Subject, Student, Date

admin.site.register(Mark)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Date)

