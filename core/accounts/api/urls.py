# -*- coding: utf-8; -*-
#
# alisaidomar <saidomarali@mail.com>
# pylint: disable=invalid-name
"""
urls modules
"""

from django.urls import path

from . import views

urlpatterns = [
    path('companies/', views.CompaniesListView.as_view(),
         name='manage_companies'),
    path('companies/<int:pk>', views.CompanyView.as_view(),
         name='manage_company'),

    path('companies/<int:company>/phones',
         views.CompaniesPhonesListView.as_view(),
         name='manage_company_phones'),
    path('companies/<int:company>/phones/<int:pk>',
         views.CompanyPhoneView.as_view(),
         name='manage_company_phone'),

    path('companies/<int:company>/addresses',
         views.CompaniesAddressListView.as_view(),
         name='manage_company_addresses'),
    path('companies/<int:company>/addresses/<int:pk>',
         views.CompanyAddressView.as_view(),
         name='manage_company_address'),

    path('companies/<int:company>/accounts',
         views.AccountListView.as_view(),
         name='manage_company_accounts'),
    path('companies/<int:company>/accounts/<int:pk>',
         views.AccountView.as_view(),
         name='manage_company_account'),

    path('companies/<int:company>/accounts/<int:account>/roles',
         views.MemberRoleListView.as_view(),
         name='manage_account_roles'),
    path('companies/<int:company>/accounts/<int:account>/roles/<int:pk>',
         views.MemberRoleView.as_view(),
         name='manage_account_role'),

    path('members', views.MemberListView.as_view(),
         name='manage_members'),
    path('members/<int:pk>', views.MemberView.as_view(),
         name='manage_member'),
]
