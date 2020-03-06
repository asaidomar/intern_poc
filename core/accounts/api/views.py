# -*- coding: utf-8; -*-
#
# https://imaginhome.icade.fr icade All rights reserved.
# alisaidomar <saidomarali@mail.com>
# 19/07/2018
# pylint: disable=no-member
# pylint: disable=no-self-use

"""
Views module
"""
from rest_framework import generics

import logger


# pylint: disable=invalid-name
from core.accounts.api.serializers import CompanySerializer, CompanyPhoneSerializer, CompanyAddressSerializer, \
    AccountSerializer, RoleSerializer, MemberSerializer
from core.accounts.models import Company, CompanyPhone, CompanyAddress, Account, Role, Member

op_logger = logger.get_logger(__file__)


class CompaniesListView(generics.ListCreateAPIView):
    """ List companies view """
    serializer_class = CompanySerializer
    queryset = Company.objects.filter()


class CompanyView(generics.RetrieveUpdateDestroyAPIView):
    """ RUD on company resource"""
    serializer_class = CompanySerializer
    lookup_url_kwarg = 'pk'
    queryset = Company.objects.filter()


class CompaniesPhonesListView(generics.ListCreateAPIView):
    """ CR on company phones """
    serializer_class = CompanyPhoneSerializer
    lookup_url_kwarg = "company"

    def get_queryset(self):
        company = self.kwargs.get(self.lookup_url_kwarg)
        phones = CompanyPhone.objects.filter(company=company)
        return phones


class CompanyPhoneView(generics.RetrieveUpdateDestroyAPIView):
    """ RUD on company phone resource"""
    serializer_class = CompanyPhoneSerializer
    lookup_url_kwarg = 'pk'
    queryset = CompanyPhone.objects.filter()


class CompaniesAddressListView(generics.ListCreateAPIView):
    """ CR on company addresses """
    serializer_class = CompanyAddressSerializer
    lookup_url_kwarg = "company"

    def get_queryset(self):
        company = self.kwargs.get(self.lookup_url_kwarg)
        phones = CompanyAddress.objects.filter(company=company)
        return phones


class CompanyAddressView(generics.RetrieveUpdateDestroyAPIView):
    """ RUD on company address resource"""
    serializer_class = CompanyAddressSerializer
    lookup_url_kwarg = 'pk'
    queryset = CompanyAddress.objects.filter()


class AccountListView(generics.ListCreateAPIView):
    """ CR on company addresses """
    serializer_class = AccountSerializer
    lookup_url_kwarg = "company"

    def get_queryset(self):
        company = self.kwargs.get(self.lookup_url_kwarg)
        phones = Account.objects.filter(company=company)
        return phones


class AccountView(generics.RetrieveUpdateDestroyAPIView):
    """ RUD on company address resource"""
    serializer_class = AccountSerializer
    lookup_url_kwarg = 'pk'
    queryset = Account.objects.filter()


class MemberRoleListView(generics.ListCreateAPIView):
    """ CR on account roles """
    serializer_class = MemberSerializer
    lookup_url_kwarg = 'account'

    def get_queryset(self):
        account = self.kwargs.get(self.lookup_url_kwarg)
        roles = Role.objects.filter(account=account)
        return Member.objects.filter(roles__in=roles)


class MemberRoleView(generics.RetrieveUpdateDestroyAPIView):
    """ RUD on account roles resource """
    serializer_class = MemberSerializer
    lookup_url_kwarg = 'pk'
    queryset = Member.objects.filter()


class MemberListView(generics.ListAPIView):
    """ R on member """
    serializer_class = MemberSerializer

    def get_queryset(self):
        roles = Member.objects.filter(roles__isnull=False)
        return roles


class MemberView(generics.RetrieveAPIView):
    """ R on member resource """
    serializer_class = MemberSerializer
    lookup_url_kwarg = 'pk'
    queryset = Member.objects.filter()
