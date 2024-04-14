from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, attrs):
        if not attrs['title'].isalpha():
            raise serializers.ValidationError('Title must be alphabet')
        if attrs['title'] == attrs['description']:
            raise serializers.ValidationError('Title and Description must be different')
        if attrs['price'] < 0:
            raise serializers.ValidationError('Price must be greater than 0')
        return attrs


class QuestionSerializer(serializers.Serializer):
    question_text = serializers.CharField(max_length=200)
    question_category = serializers.CharField(max_length=200)
