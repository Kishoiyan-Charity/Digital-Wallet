from django.contrib import admin
from .models import Account, Card, Currency, Customer, Loan, Notification, Receipt, Reward, Third_party, Transaction, Wallet

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name", "last_name",)
    search_fields=("first_name", "last_name",)

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Receipt)
admin.site.register(Card)
admin.site.register(Third_party)
admin.site.register(Notification)
admin.site.register(Loan)
admin.site.register(Reward)
admin.site.register(Currency)
