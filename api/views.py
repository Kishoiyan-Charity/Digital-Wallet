from msilib.schema import Class
from rest_framework import viewsets
from wallet.models import Customer
from serializer import CustomerSerializer

# Create your views here.
class CustomerViewset(viewsets.ModelViewset):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
