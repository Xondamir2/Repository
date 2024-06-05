from rest_framework import serializers
from .models import Teacher, Student, Clas



class ClasSerializerClass(serializers.Serializer):
    name = serializers.CharField(max_length=255)


    def create(self, validated_data):
        return Clas.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)


class TeacherSerializerClass(serializers.Serializer):
    full_name = serializers.CharField(max_length=255)
    price = serializers.IntegerField()
    clas_id = serializers.IntegerField()


    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.price = validated_data.get('price', instance.price)
        instance.clas_id = validated_data.get('clas_id', instance.clas_id)


class StudentSerializerClass(serializers.Serializer):
    full_name = serializers.CharField(max_length=255)
    clas_id = serializers.IntegerField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.clas_id = validated_data.get('clas_id', instance.clas_id)