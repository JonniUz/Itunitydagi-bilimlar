from rest_framework import serializers
from .models import Group, Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    persons = PersonSerializer(read_only=True, many=True)

    class Meta:
        model = Group
        fields = '__all__'
