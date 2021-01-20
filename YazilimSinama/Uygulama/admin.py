from django.contrib import admin
from .models import JobList
from .models import Todos
# Register your models here.
admin.site.register(JobList)
admin.site.register(Todos)
