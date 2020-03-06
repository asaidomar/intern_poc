# -*- coding: utf-8; -*-
#

""" DRF serializers """
from django.contrib.auth.models import User
from rest_framework import serializers

from core.accounts.models import (
    Company, CompanyAddress, CompanyPhone, Account, Role, Member)


class CompanyAddressSerializer(serializers.ModelSerializer):
    """ `core.accounts.models.CompanyAddress` serializer """

    class Meta:
        """ Meta """
        model = CompanyAddress
        fields = '__all__'
        read_only_fields = ("pk", )


class CompanyPhoneSerializer(serializers.ModelSerializer):
    """ `core.accounts.models.CompanyPhone` serializer """
    class Meta:
        """
        Meta
        """
        model = CompanyPhone
        fields = '__all__'
        read_only_fields = ("pk", )


class CompanySerializer(serializers.ModelSerializer):
    """ `core.accounts.models.Company` serializer. """

    class Meta:
        """ Meta """
        model = Company
        fields = '__all__'
        read_only_fields = ("pk", )


class AccountSerializer(serializers.ModelSerializer):
    """ `core.accounts.models.Account` serializer. """

    class Meta:
        """ Meta """
        model = Account
        fields = '__all__'
        read_only_fields = ("pk", )


class RoleSerializer(serializers.ModelSerializer):
    """ `core.accounts.models.Role` serializer. """
    class Meta:
        """ Meta """
        model = Role
        fields = '__all__'
        read_only_fields = ("pk", )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        """ Meta """
        model = User

        fields = ("first_name", "last_name", "groups", "email")
        read_only_fields = ("pk", )


class MemberSerializer(serializers.ModelSerializer):

    roles = RoleSerializer(many=True)
    user = UserSerializer()

    class Meta:
        """ Meta """
        model = Member
        fields = "__all__"
        read_only_fields = ("pk", )
