from django.urls import path
from . import views

urlpatterns=[
    path('showbank/<int:pk>/' , views.ShowBank.as_view() , name='showbank'),
    path('<int:pk>/bankdetails/' , views.bankdetail.as_view() , name='bankdetails'),
    path('<int:pk>/branchdetails/' , views.branchdetail.as_view() , name='branchdetails'),
    path('addbank/' , views.addbank.as_view() , name='addbank'),  
    path('<int:pk>/addbranch/' , views.addbranch.as_view() , name='addbranch')  ,
    path('<int:pk>/editbranch/' , views.aditbranch.as_view() , name='editbranch')  ,
    # path('Userprofile/' , views.Userprofile.as_view() , name='Userprofile')  ,
 ]

