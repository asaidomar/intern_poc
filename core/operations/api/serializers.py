#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# filename : serializers
# project: intern
# author : alisaidomar
""" DRF serializers """
from rest_framework import serializers

from core.operations.models import (
    Invoice, Payment, Misc, Credit, Unpaid, Recovery, Action, Lettering, Operation)


class InvoiceSerializer(serializers.ModelSerializer):
    """ `core.operations.models.Invoice` serializer """

    class Meta:
        """ Meta """
        model = Invoice
        fields = '__all__'
        read_only_fields = ("pk", )


class PaymentSerializer(serializers.ModelSerializer):
    """ `core.operations.models.Payment` serializer """

    class Meta:
        """ Meta """
        model = Payment
        fields = '__all__'
        read_only_fields = ("pk", )


class MiscSerializer(serializers.ModelSerializer):
    """ `core.operations.models.Misc` serializer """

    class Meta:
        """ Meta """
        model = Misc
        fields = '__all__'
        read_only_fields = ("pk", )


class CreditSerializer(serializers.ModelSerializer):
    """ `core.operations.models.Credit` serializer """

    class Meta:
        """ Meta """
        model = Credit
        fields = '__all__'
        read_only_fields = ("pk", )


class UnpaidSerializer(serializers.ModelSerializer):
    """ `core.operations.models.Unpaid` serializer """

    class Meta:
        """ Meta """
        model = Unpaid
        fields = '__all__'
        read_only_fields = ("pk", )

        
class RecoverySerializer(serializers.ModelSerializer):
    """ `core.operations.models.Recovery` serializer """

    class Meta:
        """ Meta """
        model = Recovery
        fields = '__all__'
        read_only_fields = ("pk", )


class ActionSerializer(serializers.ModelSerializer):
    """ `core.operations.models.Action` serializer """

    class Meta:
        """ Meta """
        model = Action
        fields = '__all__'
        read_only_fields = ("pk", )
        

class LetteringSerializer(serializers.ModelSerializer):
    """ `core.operations.models.Lettering` serializer """

    class Meta:
        """ Meta """
        model = Lettering
        fields = '__all__'
        read_only_fields = ("pk", )
        
        
class OperationSerializer(serializers.ModelSerializer):
    """ `core.operations.models.Operation` serializer """

    class Meta:
        """ Meta """
        model = Operation
        fields = '__all__'
        read_only_fields = ("pk", )
