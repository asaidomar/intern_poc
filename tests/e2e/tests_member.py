#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : tests_member
# project: intern
# author : alisaidomar
import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.urls('config.urls.api')
@pytest.mark.django_db
class TestMemberAPI:

    def setup_method(self):
        self.client = APIClient()

    def test_get_member(self, create_member):
        ret = self.client.get(path=reverse("manage_member",
                                           kwargs={'pk': create_member.pk}))
        assert ret.status_code == 200
        assert ret.json()["user"]["first_name"] == create_member.user.first_name

    def test_get_members(self):
        ret = self.client.get(path=reverse("manage_members"))
        assert ret.status_code == 200

    def test_get_roles(self, create_member):
        role = create_member.roles.first()
        company = role.company
        account = role.account

        path = reverse(
            "manage_account_roles",
            kwargs={'company': company.pk, 'account': account.pk})

        ret = self.client.get(path)

        assert ret.status_code == 200
