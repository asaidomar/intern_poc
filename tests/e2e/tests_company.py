#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : __init__.py
# project: intern
# author : alisaidomar
from datetime import datetime

import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.urls('config.urls.api')
@pytest.mark.django_db
class TestCompanyAPI:

    def setup_method(self):
        self.client = APIClient()

    def test_create_company(self):
        company_data = {
            "system_creation_date": "2020-03-05",
            "name": "TEST",
            "tva_number": "12435367373FR",
            "code": "36346664",
            "siret": "12435367373",
            "code_naf": "TEST",
            "activity": "TEST",
            "employee_number": 1,
            "creation_date": "2020-03-05",
            "url": None,
            "parent": None
        }

        ret = self.client.post(path=reverse("manage_companies"),
                               data=company_data, format="json")
        assert ret.status_code == 201
        company_json = ret.json()
        del company_json["id"]

        company_data["update_date"] = datetime.now().strftime("%Y-%m-%d")
        assert company_json == company_data

    def test_get_company(self, create_company):
        ret = self.client.get(path=reverse("manage_company",
                                           kwargs={'pk': create_company.pk}))
        assert ret.status_code == 200
        assert ret.json()["tva_number"] == create_company.tva_number

    def test_delete_company(self, create_company):
        ret = self.client.delete(path=reverse("manage_company",
                                              kwargs={'pk': create_company.pk}))

        assert ret.status_code == 204
        assert self.client.get(
            path=reverse("manage_company",
                         kwargs={'pk': create_company.pk})).status_code == 404

    def test_patch_company(self, create_company):
        new_name = create_company.name + "_NEW"
        ret = self.client.patch(
            path=reverse(
                "manage_company",
                kwargs={'pk': create_company.pk}),
            data={"name": new_name}
        )

        assert ret.status_code == 200
        create_company.refresh_from_db()
        assert create_company.name == new_name

    def test_create_company_phone(self, create_company):
        phone_data = {"value": "088989089", "company": create_company.pk}
        ret = self.client.post(
            path=reverse(
                "manage_company_phones",
                kwargs={'company': create_company.pk}),
            data=phone_data,
            format="json")

        assert ret.status_code == 201
        phone_json = ret.json()
        del phone_json["id"]
        assert phone_json == phone_data

    def test_get_company_phone(self, create_phone):
        ret = self.client.get(path=reverse(
            "manage_company_phone",
            kwargs={'pk': create_phone.pk, 'company': create_phone.company.pk}))
        assert ret.status_code == 200
        assert ret.json()["value"] == create_phone.value

    def test_get_company_phones(self, create_phone):
        ret = self.client.get(path=reverse(
            "manage_company_phones",
            kwargs={'company': create_phone.company.pk}))
        assert ret.status_code == 200
        assert ret.json()[0]["value"] == create_phone.value

    def test_update_company_phone(self, create_phone):
        new_value = create_phone.value + "00"
        phone_data = {"value": new_value, "company": create_phone.company.pk}
        ret = self.client.put(
            path=reverse(
                "manage_company_phone",
                kwargs={
                    'pk': create_phone.pk,
                    'company': create_phone.company.pk
                }
            ),
            data=phone_data
        )
        assert ret.status_code == 200
        create_phone.refresh_from_db()
        assert create_phone.value == new_value

    def test_delete_company_phone(self, create_phone):
        path = reverse(
            "manage_company_phone",
            kwargs={'pk': create_phone.pk, 'company': create_phone.company.pk}
        )
        ret = self.client.delete(path)
        assert ret.status_code == 204
        assert self.client.get(path=path).status_code == 404

    def test_create_company_address(self, create_company):
        address_data = {
            "main_address": True,
            "address": "129 rue de machin",
            "city": "MARSEILLE",
            "country": "FRANCE",
            "zip_code": "13007",
            "company": create_company.pk}
        ret = self.client.post(
            path=reverse(
                "manage_company_addresses",
                kwargs={'company': create_company.pk}),
            data=address_data,
            format="json")

        assert ret.status_code == 201
        address_json = ret.json()
        del address_json["id"]
        assert address_json == address_data

    def test_get_company_address(self, create_address):
        ret = self.client.get(path=reverse(
            "manage_company_address",
            kwargs={
                'pk': create_address.pk,
                'company': create_address.company.pk
            }
        ))
        assert ret.status_code == 200
        assert ret.json()["address"] == create_address.address

    def test_get_company_addresses(self, create_address):
        ret = self.client.get(path=reverse(
            "manage_company_addresses",
            kwargs={'company': create_address.company.pk}))
        assert ret.status_code == 200
        assert ret.json()[0]["address"] == create_address.address

    def test_update_company_address(self, create_address):
        new_value = create_address.address + "NEW"
        address_data = {"address": new_value}
        ret = self.client.patch(path=reverse(
            "manage_company_address",
            kwargs={
                'pk': create_address.pk,
                'company': create_address.company.pk}),
            data=address_data)
        assert ret.status_code == 200
        create_address.refresh_from_db()
        assert create_address.address == new_value

    def test_delete_company_address(self, create_address):
        path = reverse(
            "manage_company_address",
            kwargs={
                'pk': create_address.pk,
                'company': create_address.company.pk
            }
        )
        ret = self.client.delete(path)
        assert ret.status_code == 204
        assert self.client.get(path=path).status_code == 404

    def test_create_company_account(self, create_company):
        account_data = {
            "code": "233453553",
            "iban": "25353563GRDFFDFD",
            "bank": "SG",
            "company": create_company.pk,
        }
        ret = self.client.post(
            path=reverse(
                "manage_company_accounts",
                kwargs={'company': create_company.pk}),
            data=account_data,
            format="json")

        assert ret.status_code == 201
        account_json = ret.json()
        del account_json["id"]
        assert account_json == account_data

    def test_get_company_account(self, create_account):
        ret = self.client.get(path=reverse(
            "manage_company_account",
            kwargs={
                'pk': create_account.pk,
                'company': create_account.company.pk
            }
        ))
        assert ret.status_code == 200
        assert ret.json()["iban"] == create_account.iban

    def test_get_company_accounts(self, create_account):
        ret = self.client.get(path=reverse(
            "manage_company_accounts",
            kwargs={'company': create_account.company.pk}))
        assert ret.status_code == 200
        assert ret.json()[0]["iban"] == create_account.iban

    def test_update_company_account(self, create_account):
        new_value = create_account.bank + "NEW"
        account_data = {"bank": new_value}
        ret = self.client.patch(path=reverse(
            "manage_company_account",
            kwargs={
                'pk': create_account.pk,
                'company': create_account.company.pk}),
            data=account_data)
        assert ret.status_code == 200
        create_account.refresh_from_db()
        assert create_account.bank == new_value

    def test_delete_company_account(self, create_account):
        path = reverse(
            "manage_company_account",
            kwargs={
                'pk': create_account.pk,
                'company': create_account.company.pk
            }
        )
        ret = self.client.delete(path)
        assert ret.status_code == 204
        assert self.client.get(path=path).status_code == 404
