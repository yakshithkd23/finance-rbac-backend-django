from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import FinancialRecord
from .serializers import FinancialRecordSerializer
from users.permissions import IsAdmin, IsAnalystOrAdmin

class FinancialRecordViewSet(viewsets.ModelViewSet):
    """
    Handles CRUD operations for financial records
    """

    queryset = FinancialRecord.objects.all()
    serializer_class = FinancialRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        """
        Role-based access control
        """
        if self.action in ['create', 'update', 'destroy']:
            return [IsAdmin()]
        return [IsAnalystOrAdmin()]

    def get_queryset(self):
        """
        Filtering logic
        """
        queryset = super().get_queryset()

        category = self.request.query_params.get('category')
        record_type = self.request.query_params.get('type')

        if category:
            queryset = queryset.filter(category=category)
        if record_type:
            queryset = queryset.filter(type=record_type)

        return queryset