#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# filename : views
# project: intern
# author : alisaidomar
from rest_framework import generics
from .. import signals  # noqa

import logger


# pylint: disable=invalid-name
from core.operations.api.serializers import (
    InvoiceSerializer, PaymentSerializer, CreditSerializer, UnpaidSerializer,
    MiscSerializer, ActionSerializer, RecoverySerializer, LetteringSerializer,
    OperationSerializer)
from core.operations.models import (
    Invoice, Payment, Credit, Lettering, Unpaid, Misc,
    Action, Recovery, Operation)

op_logger = logger.get_logger(__file__)


class InvoiceListView(generics.ListCreateAPIView):
    """ List Invoices view """
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.filter()

    lookup_url_kwarg = "account"

    def get_queryset(self):
        account = self.kwargs.get(self.lookup_url_kwarg)
        phones = Invoice.objects.filter(company=account)
        return phones


class InvoiceView(generics.RetrieveUpdateDestroyAPIView):
    """ RUD on company resource"""
    # TODO: check status, avoid update, delete if invoice has been sent
    serializer_class = InvoiceSerializer
    lookup_url_kwarg = 'pk'
    queryset = Invoice.objects.filter()


class PaymentListView(generics.ListCreateAPIView):
    """ List Payments view """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.filter()

    lookup_url_kwarg = "account"

    def get_queryset(self):
        account = self.kwargs.get(self.lookup_url_kwarg)
        phones = Payment.objects.filter(company=account)
        return phones


class PaymentView(generics.RetrieveUpdateDestroyAPIView):
    """ RUD on company resource"""
    # TODO: check status, avoid update, delete if Payment has been sent
    serializer_class = PaymentSerializer
    lookup_url_kwarg = 'pk'
    queryset = Payment.objects.filter()


class CreditListView(generics.ListCreateAPIView):
    """ List Credits view """
    serializer_class = CreditSerializer
    queryset = Credit.objects.filter()
    lookup_url_kwarg = "account"

    def get_queryset(self):
        account = self.kwargs.get(self.lookup_url_kwarg)
        phones = Credit.objects.filter(company=account)
        return phones


class CreditView(generics.RetrieveUpdateDestroyAPIView):
    """ RUD on credit resource"""
    # TODO: check status, avoid update, delete if Credit has been sent
    serializer_class = CreditSerializer
    lookup_url_kwarg = 'pk'
    queryset = Credit.objects.filter()
    
    
class LetteringListView(generics.ListCreateAPIView):
    """ List Letterings view """
    serializer_class = LetteringSerializer
    queryset = Lettering.objects.filter()
    lookup_url_kwarg = "account"

    def get_queryset(self):
        account = self.kwargs.get(self.lookup_url_kwarg)
        phones = Lettering.objects.filter(company=account)
        return phones


class LetteringView(generics.RetrieveUpdateDestroyAPIView):
    """ RUD on Lettering resource"""
    serializer_class = LetteringSerializer
    lookup_url_kwarg = 'pk'
    queryset = Lettering.objects.filter()

    
class UnpaidListView(generics.ListCreateAPIView):
    """ List Unpaids view """
    serializer_class = UnpaidSerializer
    queryset = Unpaid.objects.filter()

    lookup_url_kwarg = "account"

    def get_queryset(self):
        account = self.kwargs.get(self.lookup_url_kwarg)
        phones = Unpaid.objects.filter(company=account)
        return phones


class UnpaidView(generics.RetrieveUpdateDestroyAPIView):
    """ RUD on Unpaid resource"""
    serializer_class = UnpaidSerializer
    lookup_url_kwarg = 'pk'
    queryset = Unpaid.objects.filter()
    
    
class MiscListView(generics.ListCreateAPIView):
    """ List Miscs view """
    serializer_class = MiscSerializer
    queryset = Misc.objects.filter()

    lookup_url_kwarg = "account"

    def get_queryset(self):
        account = self.kwargs.get(self.lookup_url_kwarg)
        phones = Misc.objects.filter(company=account)
        return phones


class MiscView(generics.RetrieveUpdateDestroyAPIView):
    """ RUD on Misc resource"""
    serializer_class = MiscSerializer
    lookup_url_kwarg = 'pk'
    queryset = Misc.objects.filter()


class ActionListView(generics.ListCreateAPIView):
    """ List Actions view """
    serializer_class = ActionSerializer
    queryset = Action.objects.filter()
    lookup_url_kwarg = "account"

    def get_queryset(self):
        account = self.kwargs.get(self.lookup_url_kwarg)
        phones = Action.objects.filter(company=account)
        return phones


class ActionView(generics.RetrieveUpdateDestroyAPIView):
    """ RUD on Action resource"""
    serializer_class = ActionSerializer
    lookup_url_kwarg = 'pk'
    queryset = Action.objects.filter()
    
    
class RecoveryListView(generics.ListCreateAPIView):
    """ List Recoverys view """
    serializer_class = RecoverySerializer
    queryset = Recovery.objects.filter()
    lookup_url_kwarg = "account"

    def get_queryset(self):
        account = self.kwargs.get(self.lookup_url_kwarg)
        phones = Recovery.objects.filter(company=account)
        return phones


class RecoveryView(generics.RetrieveUpdateDestroyAPIView):
    """ RUD on Recovery resource"""
    serializer_class = RecoverySerializer
    lookup_url_kwarg = 'pk'
    queryset = Recovery.objects.filter()


class OperationListView(generics.ListCreateAPIView):
    """ List Operations view """
    serializer_class = OperationSerializer
    queryset = Operation.objects.filter()
    lookup_url_kwarg = "account"

    def get_queryset(self):
        account = self.kwargs.get(self.lookup_url_kwarg)
        phones = Operation.objects.filter(company=account)
        return phones


class OperationView(generics.RetrieveUpdateDestroyAPIView):
    """ RUD on Operation resource"""
    serializer_class = OperationSerializer
    lookup_url_kwarg = 'pk'
    queryset = Operation.objects.filter()
