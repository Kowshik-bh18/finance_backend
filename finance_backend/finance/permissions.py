from rest_framework.permissions import BasePermission

class FinancialRecordPermission(BasePermission):
    def has_permission(self, request, view):

        if request.user.role == 'VIEWER':
            return request.method in ['GET']

        elif request.user.role == 'ANALYST':
            return request.method in ['GET']

        elif request.user.role == 'ADMIN':
            return True

        return False