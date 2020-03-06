#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# filename : fake_data
# project: intern
# author : alisaidomar
from datetime import datetime

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from mixer.backend.django import mixer

from core.accounts.models import (
    Company, CompanyPhone, CompanyAddress, Role, Member, Account)
from core.operations.models import Invoice, Payment, Lettering


def create_company():
    company_obj = mixer.blend(
        Company,
        system_creation_date=datetime.now(),
        name=mixer.faker.company,
    )
    return company_obj


def create_phone(create_company):
    company_phone = mixer.blend(
        CompanyPhone, company=create_company, code=mixer.faker.bban)
    return company_phone


def create_address(create_company):
    company_address = mixer.blend(
        CompanyAddress, company=create_company, main_address=True)
    return company_address


def create_account(company):
    account = mixer.blend(Account, company=company)
    return account


def create_role(create_account):
    role = mixer.blend(
        Role, account=create_account, company=create_account.company)
    return role


def create_member(create_role):
    member = mixer.blend(Member, user=mixer.blend(User))
    member.roles.add(create_role)
    return member


def create_invoice(account, company):
    invoice = mixer.blend(Invoice, account=account, client=company)
    return invoice


def create_payment(account):
    payment = mixer.blend(Payment, account=account)
    return payment


def create_lettering(create_account):
    lettering = mixer.blend(Lettering, account=create_account)
    return lettering


def generate_compagnies(n_compagnies):
    for i in range(n_compagnies):
        yield create_company()


class Command(BaseCommand):
    help = 'GENERATE FAKE DATE'

    def add_arguments(self, parser):
        pass
        #parser.add_argument('poll_ids', , type=int)

    def handle(self, *args, **options):
        for c in generate_compagnies(10):
            acc = create_account(c)
            for _ in range(100):
                pay = create_payment(acc)
                invoice = create_invoice(acc, c)




