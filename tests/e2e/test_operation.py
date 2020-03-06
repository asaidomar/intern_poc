#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) JOHN PAUL (https://www.johnpaul.com/) all rights reserved.
# filename : test_operation
# date : 2020-03-06-14-39
# project: intern
# author : alisaidomar
import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from core.operations.models import Operation, Invoice


@pytest.mark.urls('config.urls.api')
@pytest.mark.django_db
class TestOperationAPI:
    def setup_method(self):
        self.client = APIClient()

    def test_create_invoice(self, create_account, create_company):
        invoice_data = {
            "status": "draf",
            "number": "20010",
            "emit_date": "2020-05-31",
            "days_delays": 60,
            "amount": 300,
            "client": create_company.pk,
            "account": create_account.pk
        }
        path = reverse("manage_invoices", kwargs={"account": create_account.pk})
        ret = self.client.post(path=path,
                               data=invoice_data, format="json")
        assert ret.status_code == 201
        assert Operation.objects.first().invoice.pk == ret.json()["id"]

    def test_create_payment(self, create_account):
        invoice_data = {
            "payment_type": "cash",
            "amount": 300,
            "account": create_account.pk
        }
        path = reverse("manage_payments", kwargs={"account": create_account.pk})
        ret = self.client.post(path, data=invoice_data, format="json")
        assert ret.status_code == 201
        assert Operation.objects.first().payment.pk == ret.json()["id"]

    def test_lettering_payment(self, create_account):
        invoice_data = {
            "code": "AD_300",
        }
        path = reverse("manage_letterings", kwargs={"account": create_account.pk})
        ret = self.client.post(path, data=invoice_data, format="json")
        assert ret.status_code == 201
        assert Operation.objects.first().payment.pk == ret.json()["id"]

    def test_operation_lettering(self, create_invoice, create_payment, create_lettering):
        operation = Operation.objects.first()

        path = reverse("manage_operation",
                       kwargs={"account": create_invoice.pk, "pk": operation.pk})
        data = {"lettering": create_lettering.pk}
        ret = self.client.patch(path, data=data, format="json")

        assert ret.status_code == 200
        assert Operation.objects.filter(lettering=create_lettering).first()
