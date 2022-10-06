from atexit import register
from unicodedata import name
from django.urls import path
from .views import  account_display, account_list, card_display, card_list, currency_list, customer_list, customer_profile, edit_account, edit_card, edit_customer, edit_receipt, edit_transaction, edit_wallet, list_customers, loan_list, notifcation_list, receipt_display, receipt_list, register_account, register_loan,register_notification, register_currency, register_customer, register_third_party, register_wallet, register_transaction,register_receipt, register_card, register_reward, reward_list, third_party_list, transaction_display, transaction_list, wallet_display, wallet_list

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

    path("list/", list_customers, name="list_customers"),

    path("customers/<int:id>/", customer_profile, name="customer_profile"),

    path("customers/edit/<int:id>/", edit_customer, name="edit_customer"),




     # Urls for displaying the content of the forms
    path('customers/', customer_list, name='customer list'),
    path('wallet-list/', wallet_list, name='wallet list'),
    path('accounts-list/', account_list, name='account list'),
    path('reward-list/', reward_list, name = 'reward list'),
    path('transaction-list/', transaction_list, name = 'transact list'),
    path('card-list/', card_list, name = 'card list'),
    path('notifcation-list/', notifcation_list, name = 'notifcation_list'),
    path('receipt-list/', receipt_list, name = 'receipt_list'),
    path('loans-list/', loan_list, name = 'loans_list'),
    path('third-party-list/', third_party_list, name = 'third_party'),
    path('currency-list/', currency_list, name = 'currency_list'),


    # URLS for displaying a single object content 
    path('profile/<int:id>', customer_profile, name='profile'),
    path('wallet-display/<int:id>', wallet_display, name='wallet-display'),
    path('account-display/<int:id>', account_display, name='account-display'),
    path('card-display/<int:id>', card_display, name='wcard-display'),
    path('transaction-display/<int:id>', transaction_display, name='transaction-display'),
    path('receipt-display/<int:id>', receipt_display, name='receipt-display'),

    # Editing customer information
    path('wallet-list/edit/<int:id>', edit_wallet, name = 'edit_wallet'),
    path('accounts-list/edit/<int:id>', edit_account, name = 'edit_account'),
    path('receipt-list/edit/<int:id>', edit_receipt, name = 'edit_receipt'),
    path('card-list/edit/<int:id>', edit_card, name = 'edit_card'),
    path('transaction-list/edit/<int:id>', edit_transaction, name = 'edit_transaction'),

]