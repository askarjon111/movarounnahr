from rest_framework import serializers
from board.models import Lead, LeadAction, Task, Telegram_user
from account.models import Company


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'


class LeadActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadAction
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name']


class Telegram_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telegram_user
        fields = '__all__'
