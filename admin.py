from django.contrib import admin

# Register your models here.
from todolist.models import todoitem

admin.site.register(todoitem)