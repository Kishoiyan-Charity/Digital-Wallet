from django.urls import path,include
from rest_framework import routers
from .views import CustomerView, CustomerViewset

router= routers.DefaultRouters()
router.register( r"customers", CustomerViewset)
urlpatterns= [
    path("", include(router.urls)),
    
]