from django.contrib import admin
from .models import Batch, Course, Student, Topic, Trainer

# Register your models here.
admin.site.register(Student)
admin.site.register(Batch)
admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(Trainer)