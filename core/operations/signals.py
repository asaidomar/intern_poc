#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# filename : signals
# project: intern
# author : alisaidomar
import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver

from core.operations.models import Invoice, Operation, Payment, Credit, Unpaid, Misc


@receiver(post_save, sender=Invoice, dispatch_uid="creation_invoice_operation_item")
def save_operation_invoice(sender, **kwargs):
    """ creates operation entry after invoice creation """
    instance = kwargs.get("instance")
    if kwargs.get("created"):
        due_date = instance.creation_date + datetime.timedelta(
            days=instance.days_delays)
        return Operation(
            operation_type=Operation.invoice,
            debit_amount=instance.amount,
            credit_amount=0,
            account=instance.account,
            invoice=instance, due_date=due_date).save()


@receiver(post_save, sender=Payment, dispatch_uid="creation_payment_operation_item")
def save_operation_payment(sender, **kwargs):
    """ creates operation entry after payment creation """
    instance = kwargs.get("instance")
    if kwargs.get("created"):
        return Operation(
            operation_type=Operation.payment,
            credit_amount=instance.amount,
            debit_amount=0,
            account=instance.account,
            payment=instance).save()


@receiver(post_save, sender=Credit, dispatch_uid="creation_credit_operation_item")
def save_operation_credit(sender, instance: Credit, **kwargs):
    """ creates operation entry after credit creation """
    if kwargs.get("created"):
        return Operation(
            operation_type=Operation.credit,
            debit_amount=instance.amount,
            credit=instance).save()


@receiver(post_save, sender=Unpaid, dispatch_uid="creation_unpaid_operation_item")
def save_operation_unpaid(sender, instance: Unpaid, **kwargs):
    """ creates operation entry after Unpaid creation """
    if kwargs.get("created"):
        return Operation(
            operation_type=Operation.credit,
            debit_amount=instance.debit_amount,
            credit=instance).save()


@receiver(post_save, sender=Misc, dispatch_uid="creation_misc_operation_item")
def save_operation_misc(sender, instance: Misc, **kwargs):
    """ creates operation entry after Unpaid creation """
    if kwargs.get("created"):
        return Operation(
            operation_type=Operation.credit,
            debit_amount=instance.debit_amount,
            credit_amount=instance.credit_amount,
            misc_operation=instance).save()
