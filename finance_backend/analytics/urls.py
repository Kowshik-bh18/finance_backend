from django.urls import path
from .views import *

urlpatterns = [
    path('summary/', SummaryView.as_view()),
    path('category/', CategorySummaryView.as_view()),
    path('trends/', MonthlyTrendView.as_view()),
    path('recent/', RecentActivityView.as_view()),
    path('top-category/', TopSpendingCategory.as_view()),
]