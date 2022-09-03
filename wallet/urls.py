from atexit import register
from unicodedata import name
from django.urls import path
from .views import register_account, register_loan,register_notification, register_currency, register_customer, register_third_party, register_wallet, register_transaction,register_receipt, register_card, register_reward

urlpatterns=[
    path("register/", register_customer, name="registration"),

    path("currency/", register_currency, name="registercurrency"),

    path("wallet/", register_wallet, name="registerwallet"),

    path("account/", register_account, name="registeraccount"),

    path("transaction/", register_transaction, name="registertransaction"),

    path("receipt/", register_receipt, name="registerreceipt"),

    path("card/", register_card, name="registercard"),

    path("third_party/", register_third_party, name="registerthird_party"),

    path("notification/", register_notification,name="registernotification" ),

    path("loan/", register_loan, name="registerloan"),

    path("reward/", register_reward, name="registerreward"),
]