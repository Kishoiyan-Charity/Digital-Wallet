from django.contrib import admin
from .models import Account, Card, Currency, Customer, Loan, Notification, Receipt, Reward, Third_party, Transaction, Wallet

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name", "last_name",)
    search_fields=("first_name", "last_name",)
admin.site.register(Customer, CustomerAdmin)


class WalletAdmin(admin.ModelAdmin):
    list_display=("balance", "customer",)
    search_fields=("pin", "active",)
admin.site.register(Wallet, WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display=("wallet", "name",)
    search_fields=("balance", "account_type",)
admin.site.register(Account, AccountAdmin)


class TransactionAdmin(admin.ModelAdmin):
    list_display=("transaction_cost", "wallet",)
    search_fields=("transaction_type", "status",)
admin.site.register(Transaction,TransactionAdmin)

class ReceiptAdmin(admin.ModelAdmin):
    list_display=("receipt_file", "transaction",)
admin.site.register(Receipt, ReceiptAdmin)


class CardAdmin(admin.ModelAdmin):
    list_display=("Card_name", "Date_issued",)
    search_fields=("Card_number", "Signature",)
admin.site.register(Card,CardAdmin)

class Third_partyAdmin(admin.ModelAdmin):
    list_display=("account", "currency",)
    search_fields=("phonenumber", "fullname",)
admin.site.register(Third_party, Third_partyAdmin)


class NotificationAdmin(admin.ModelAdmin):
    list_display=("datecreated", "Message",)
    search_fields=("recipient", "isactive",)
admin.site.register(Notification, NotificationAdmin)


class LoanAdmin(admin.ModelAdmin):
    list_display=("loan_type", "amount",)
    search_fields=("wallet", "Interest_rate",)
admin.site.register(Loan, LoanAdmin)


class RewardAdmin(admin.ModelAdmin):
    list_display=("Points", "wallet",)
    search_fields=("date_time_received", "transaction",)
admin.site.register(Reward, RewardAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    list_display=("currency_name", "currency_symbol",)
admin.site.register(Currency, CurrencyAdmin)