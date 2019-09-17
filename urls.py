from django.contrib import admin
from django.urls import path, include
from todolist.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', todoviewset)
urlpatterns = [
    path('', include(router.urls))
]