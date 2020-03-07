#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filename : conftest
# project: intern
# author : alisaidomar
from datetime import datetime

import pytest
import os

from django.contrib.auth.models import User
from mixer.backend.django import mixer

from core.accounts.models import (
    Company, CompanyPhone, CompanyAddress, Account, Role, Member)
from core.operations.models import Invoice, Payment, Lettering


@pytest.fixture(autouse=True, scope="session")
def setup_env():
    os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.test"


@pytest.fixture
def create_company():
    company_obj = mixer.blend(Company, system_creation_date=datetime.now())
    return company_obj


@pytest.fixture
def create_phone(create_company):
    company_phone = mixer.blend(
        CompanyPhone, company=create_company, value=mixer.faker.phone_number)
    return company_phone


@pytest.fixture
def create_address(create_company):
    company_address = mixer.blend(
        CompanyAddress, company=create_company, main_address=True)
    return company_address


@pytest.fixture
def create_account(create_company):
    company_address = mixer.blend(Account, company=create_company)
    return company_address


@pytest.fixture
def create_role(create_account):
    role = mixer.blend(
        Role, account=create_account, company=create_account.company)
    return role


@pytest.fixture
def create_member(create_role):
    member = mixer.blend(Member, user=mixer.blend(User))
    member.roles.add(create_role)
    return member


@pytest.fixture
def create_invoice(create_account, create_company):
    invoice = mixer.blend(
        Invoice, account=create_account, client=create_company)
    return invoice


@pytest.fixture
def create_payment(create_account):
    payment = mixer.blend(Payment, account=create_account)
    return payment


@pytest.fixture
def create_lettering(create_account):
    lettering = mixer.blend(Lettering, account=create_account)
    return lettering
