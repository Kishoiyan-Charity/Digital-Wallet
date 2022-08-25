from django.db import models

# Create your models here.
class Currency(models.Model):
    country_origin=models.CharField(max_length=25, blank= True)
    currency_symbol=models.CharField(max_length=10 , blank= True)
    currency_name=models.CharField(max_length=20, blank= True)

class Customer(models.Model):
    id_number=models.CharField(max_length=10,blank=False, primary_key=True)
    first_name=models.CharField(max_length=15, blank=False)
    last_name=models.CharField(max_length=15, blank=False)
    gender_choices=(
        ('F','female'),
        ('M','male')
    )
    gender= models.CharField(max_length=10,choices=gender_choices,blank=False)
    address=models.TextField(max_length=15)
    age=models.PositiveSmallIntegerField()
    nationality=models.CharField(max_length=15,blank=True)
    email=models.EmailField()
    phone_number=models.CharField(max_length=15,blank=True)
    profile_picture=models.ImageField(default=False)
    marital_status=models.CharField(max_length=10, blank=True)
    signature=models.ImageField(upload_to='images/')
    employment_status=models.BooleanField(default=False)

class Wallet(models.Model):
    customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    balance=models.IntegerField()
    pin=models.PositiveSmallIntegerField()
    currency=models.ForeignKey(Currency, on_delete=models.CASCADE,related_name='wallet_currency')
    active=models.BooleanField()
    datecrated=models.DateField()
    wallet_type=models.CharField(max_length=15,)
    bank_account_name=models.CharField(max_length=15)

class Account(models.Model):
    wallet=models.ForeignKey('Wallet', on_delete=models.CASCADE,related_name='Account_wallet')
    name=models.CharField(max_length=15)
    account_type=models.CharField(max_length=15)
    balance=models.IntegerField()
    account_type=models.CharField(max_length=23)

class Transaction(models.Model):
    transaction_charge=models.CharField(max_length=3)
    transaction_cost=models.PositiveIntegerField()
    wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Transaction_wallet')
    transaction_type=models.CharField(max_length=15)
    account_origin=models.ForeignKey('Account', on_delete=models.CASCADE,related_name='Transaction_account_origin')
    account_destination=models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='Transaction_destinations')
    status=models.CharField(max_length=15)
    type=models.CharField(max_length=15)

class Receipt(models.Model):
    receipt_file=models.FileField(upload_to='media/')
    date=models.DateField()
    transaction=models.ForeignKey('Transaction',on_delete=models.CASCADE,related_name='Receipt_transaction')

class Card(models.Model):
    card_name=models.CharField(max_length=25)
    date_issued=models.DateTimeField()
    card_number=models.CharField(max_length=15)
    signature=models.CharField(max_length=15)
    expiry_date=models.DateField()
    card_status=models.CharField(max_length=15)
    security_code=models.PositiveSmallIntegerField()
    issuer=models.CharField(max_length=35)
    account=models.ForeignKey('Account', on_delete=models.CASCADE, related_name='Card_account')

class Third_party(models.Model):
    full_name=models.CharField(max_length=30)
    email=models.EmailField()
    phone_number=models.CharField(max_length=15)
    transaction_cost=models.IntegerField()
    currency=models.ForeignKey('Currency',on_delete=models.CASCADE, related_name='Third_party_currency')
    account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Third_party_account')
    active=models.BooleanField()

class Notification(models.Model):
    date_created=models.DateField()
    time=models.TimeField()
    message=models.CharField(max_length=40)
    is_active=models.BooleanField()
    image=models.ImageField()
    recipient=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='Notification_recipient')

class Loan(models.Model):
    interest=models.IntegerField()
    loan_type=models.CharField(max_length=15)
    amount=models.IntegerField()
    wallet=models.ForeignKey('Wallet', on_delete=models.CASCADE,related_name='Loan_wallet')
    due_date=models.DateField()
    loan_term=models.CharField(max_length=35)
    interest_rate=models.IntegerField()
    payment_date=models.DateField()
    duration=models.CharField(max_length=25)
    balance=models.IntegerField()
    loan_status=models.CharField(max_length=25)
    guaranter=models.CharField(max_length=25)

class Reward(models.Model):
    points=models.PositiveIntegerField()
    wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE, related_name='Reward_wallet')
    date_time_received=models.DateTimeField()
    transaction=models.ForeignKey('Transaction',on_delete=models.CASCADE,related_name='Reward_transaction')