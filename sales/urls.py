
from django.urls import path
from sales.views import listorders

from . import views

urlpatterns =[
    path('orders/',views.listorders),
    path('orders2/',views.listorders2),
    path('customers/',views.listcustomers),
]
