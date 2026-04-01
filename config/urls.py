from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from records.views import FinancialRecordViewSet
from dashboard.views import DashboardSummaryView

router = DefaultRouter()
router.register(r'records', FinancialRecordViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/dashboard/', DashboardSummaryView.as_view()),
]