from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Bank(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_banks')
    name=models.CharField(max_length=100 , null=False)
    swift_code=models.CharField(max_length=100,null=False)
    institution_number=models.CharField(max_length=100,null=False)
    discription=models.CharField(max_length=100 ,null=False)

    def __str__(self):
        return self.name
    

class Branch(models.Model):
    bank=models.ForeignKey(Bank , on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=False)
    transition_number=models.CharField(max_length=100,null=False)
    address=models.CharField(max_length=100,null=False)
    email=models.CharField(max_length=100, default='admin@enigmatix.io',null=False)
    capacity=models.PositiveIntegerField(null=False)
    last_modified=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    


