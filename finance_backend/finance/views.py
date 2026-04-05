from rest_framework.viewsets import ModelViewSet
from .models import FinancialRecord
from .serializers import FinancialRecordSerializer
from .permissions import FinancialRecordPermission
from django_filters.rest_framework import DjangoFilterBackend
class FinancialRecordViewSet(ModelViewSet):
    queryset = FinancialRecord.objects.all()   
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type', 'category', 'date']
    serializer_class = FinancialRecordSerializer
    permission_classes = [FinancialRecordPermission]

    def get_queryset(self):
        return FinancialRecord.objects.filter(
        user=self.request.user,
        is_deleted=False
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()