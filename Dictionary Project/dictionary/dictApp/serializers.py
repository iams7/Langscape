from .models import Headword, POS, Meaning
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = "__all__"

class MeaningSerializer(serializers.ModelSerializer):

    class Meta:

        model = Meaning
        fields = ("id","pos","meaning")

    # def create(self, validated_data):
    #     return Headword.objects.create(**validated_data)
class POSSerializer(serializers.ModelSerializer):

    dictionary_meanings = MeaningSerializer(many=True)

    class Meta:

        model = POS
        fields = ("part_of_speech","dictionary_meanings",)

class HeadwordSerializer(serializers.ModelSerializer):

    meanings =  POSSerializer(many=True)

    class Meta:
        model = Headword
        fields = ("word","meanings")
