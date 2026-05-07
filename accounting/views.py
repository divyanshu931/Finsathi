from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from .models import SalePurchase, CashBankTransaction
from .serializers import SalePurchaseSerializer, CashBankTransactionSerializer


def company_home(request):
    return render(request, "company_home.html")


class SalePurchaseViewSet(viewsets.ModelViewSet):
    queryset = SalePurchase.objects.all()
    serializer_class = SalePurchaseSerializer


class CashBankTransactionViewSet(viewsets.ModelViewSet):
    queryset = CashBankTransaction.objects.all()
    serializer_class = CashBankTransactionSerializer


def health_check(request):
    return HttpResponse("ok", content_type="text/plain")
