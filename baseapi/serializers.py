from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        # fields = ['id']
        # exclude = ['name', 'phone']



    def validate(self, student_data):
            if student_data['age'] < 18 :
                raise serializers.ValidationError({'error':"arge most be greater than 18"})
            
            if any(char.isdigit() for char in student_data['name']):
                raise serializers.ValidationError({'error':"name must be string"})

            return student_data


class CtegorySerializer(serializers.ModelSerializer):
     class Meta:
          model =Category
          fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
     category = CtegorySerializer() #forigen key 
     class Meta:
          model = Book
          fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
          model= User
          fields = ['id', 'username', 'password']

    def create(self, validated_data):
        user = User(
             username = validated_data['username'],
             )
        user.set_password(validated_data['password'])
        user.save()
        return user
          