__author__ = 'djakson'
from django.contrib import admin
from models import *

admin.site.register(Role)
admin.site.register(Project)
admin.site.register(ProjectMember)
admin.site.register(Sprint)
admin.site.register(SprintTask)
admin.site.register(TaskTracker)
admin.site.register(TaskStatus)