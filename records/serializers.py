from rest_framework import serializers
from .models import FinancialRecord

class FinancialRecordSerializer(serializers.ModelSerializer):
    """
    Handles validation and serialization
    """
    class Meta:
        model = FinancialRecord
        fields = '__all__'