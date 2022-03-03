from rest_framework import serializers
from .models import *
from board.models import Lead

class FilialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Filial
        fields = ['id', 'name']

class TypeRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeRoom
        fields = '__all__'

class RoomsSerializer(serializers.ModelSerializer):
    filial = FilialSerializer(read_only=True)
    type = TypeRoomSerializer(read_only=True)

    class Meta:
        model = Rooms
        fields = '__all__'

class LeadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lead
        fields = ['id', 'name']

class BooksSerializer(serializers.ModelSerializer):
    filial = FilialSerializer(read_only=True)
    client = LeadSerializer(read_only=True)

    class Meta:
        model = Books
        fields = '__all__'
