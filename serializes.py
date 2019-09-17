from rest_framework import serializers

from todolist.models import todoitem


class todoitemserializer(serializers.ModelSerializer):
    class Meta:
        model = todoitem
        fields = ['text', 'dtime', 'done']
