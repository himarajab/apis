from django.db.models import fields
from .models import Income
from rest_framework import serializers


class IncomeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Income
    fields=['id','date','description','amount','source']