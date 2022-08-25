from django.contrib import admin
from .models import Account, Card, Currency, Customer, Loan, Notification, Receipt, Reward, Third_party, Transaction, Wallet

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name", "last_name","gender","address","age","nationality","email","phone_number","profile_picture","marital_status","signature","employment_status")
    search_fields=("first_name", "last_name",)
admin.site.register(Customer, CustomerAdmin)


class WalletAdmin(admin.ModelAdmin):
    list_display=("balance", "customer","pin","currency","active","datecrated","wallet_type","bank_account_name")
    search_fields=("balance", "customer",)
admin.site.register(Wallet, WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display=("wallet", "name","account_type","balance","account_type")
    search_fields=("wallet", "name",)
admin.site.register(Account, AccountAdmin)


class TransactionAdmin(admin.ModelAdmin):
    list_display=("transaction_cost", "wallet","transaction_type","status","account_origin","account_destination","type","transaction_charge")
    search_fields=("transaction_cost", "wallet",)
admin.site.register(Transaction,TransactionAdmin)

class ReceiptAdmin(admin.ModelAdmin):
    list_display=("receipt_file", "transaction","date")
    search_fields=("receipt_file", "transaction",)
admin.site.register(Receipt, ReceiptAdmin)


class CardAdmin(admin.ModelAdmin):
    list_display=("card_name", "date_issued","card_number","signature","expiry_date","card_status","security_code","issuer","account")
    search_fields=("card_name", "date_issued",)
admin.site.register(Card,CardAdmin)

class Third_partyAdmin(admin.ModelAdmin):
    list_display=("account", "currency","phone_number","full_name","active","email")
    search_fields=("account", "currency",)
admin.site.register(Third_party, Third_partyAdmin)


class NotificationAdmin(admin.ModelAdmin):
    list_display=("date_created", "message","recipient","is_active","time","image")
    search_fields=("date_created", "message",)
admin.site.register(Notification, NotificationAdmin)


class LoanAdmin(admin.ModelAdmin):
    list_display=("interest", "loan_type","amount","wallet","due_date","loan_term","interest_rate","payment_date","duration","balance","loan_status","guaranter")
    search_fields=("interest", "loan_type",)
admin.site.register(Loan, LoanAdmin)


class RewardAdmin(admin.ModelAdmin):
    list_display=("points", "wallet","date_time_received","transaction")
    search_fields=("points", "wallet",)
admin.site.register(Reward, RewardAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    list_display=("currency_name", "currency_symbol","currency_name")
    search_fields=("currency_name", "currency_symbol",)
admin.site.register(Currency, CurrencyAdmin)