from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from finance.models import FinancialRecord
from rest_framework.permissions import IsAuthenticated
from django.db.models.functions import TruncMonth
class SummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        income = FinancialRecord.objects.filter(
            user=user, type='INCOME'
        ).aggregate(total=Sum('amount'))['total'] or 0

        expense = FinancialRecord.objects.filter(
            user=user, type='EXPENSE'
        ).aggregate(total=Sum('amount'))['total'] or 0

        return Response({
            "total_income": income,
            "total_expense": expense,
            "net_balance": income - expense
        })
    
class CategorySummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        data = FinancialRecord.objects.filter(user=user)\
            .values('category')\
            .annotate(total=Sum('amount'))

        return Response(data)

class MonthlyTrendView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        data = FinancialRecord.objects.filter(user=user)\
            .annotate(month=TruncMonth('date'))\
            .values('month')\
            .annotate(total=Sum('amount'))\
            .order_by('month')

        return Response(data)

class RecentActivityView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        records = FinancialRecord.objects.filter(user=user)\
            .order_by('-created_at')[:5]

        data = [
            {
                "amount": r.amount,
                "type": r.type,
                "category": r.category,
                "date": r.date
            }
            for r in records
        ]

        return Response(data)
    
class TopSpendingCategory(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        data = FinancialRecord.objects.filter(
            user=user, type='EXPENSE'
        ).values('category')\
         .annotate(total=Sum('amount'))\
         .order_by('-total')\
         .first()

        return Response(data)