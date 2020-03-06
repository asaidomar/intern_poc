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
    path('account/<int:account>/invoices/', views.InvoiceListView.as_view(),
         name='manage_invoices'),
    path('account/<int:account>/invoices/<int:pk>', views.InvoiceView.as_view(),
         name='manage_invoice'),

    path('account/<int:account>/payments/', views.PaymentListView.as_view(),
         name='manage_payments'),
    path('account/<int:account>/payments/<int:pk>', views.PaymentView.as_view(),
         name='manage_payment'),

    path('account/<int:account>/letterings/', views.LetteringListView.as_view(),
         name='manage_letterings'),
    path('account/<int:account>/lettering/<int:pk>', views.LetteringView.as_view(),
         name='manage_lettering'),

    path('account/<int:account>/operations/', views.OperationListView.as_view(),
         name='manage_operations'),
    path('account/<int:account>/operations/<int:pk>', views.OperationView.as_view(),
         name='manage_operation'),

]
