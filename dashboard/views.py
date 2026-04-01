from rest_framework.views import APIView
from rest_framework.response import Response
from records.models import FinancialRecord
from django.db.models import Sum

class DashboardSummaryView(APIView):
    """
    Provides aggregated financial insights
    """

    def get(self, request):
        records = FinancialRecord.objects.all()

        total_income = records.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
        total_expense = records.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0

        return Response({
            "total_income": total_income,
            "total_expense": total_expense,
            "net_balance": total_income - total_expense
        })