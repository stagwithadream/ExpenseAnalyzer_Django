from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime


# Create your models here.

class user_profile(models.Model):
    # Email=models.EmailField(max_length=254, primary_key=True)
    # FirstName=models.CharField(max_length=264)
    # LastName=models.CharField(max_length=264)
    # Password=models.CharField(max_length=264)
    # PhoneNo=models.IntegerField(null=True)
    # Wallet=models.IntegerField(null=True)
    # frequent_wallet_addition_amount=models.IntegerField(null=True)
    # amount_to_be_added=models.IntegerField(null=True)
      user=models.OneToOneField(User,on_delete=models.PROTECT)
      PhoneNo=models.IntegerField(null=True)
      Wallet=models.IntegerField(null=True)
      frequent_wallet_addition_amount=models.IntegerField(null=True)
      amount_to_be_added=models.IntegerField(null=True)

      def __str__(self):
          return self.user.username

class general_expenses(models.Model):
    T_id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(User,  on_delete=models.CASCADE,)
    amount=models.IntegerField()
    date_time=models.DateTimeField(default=datetime.now)
    categories=(
    (1,'Food'),
    (2,'Travel'),
    (3,'Groceries'),
    (4, 'Electronics'),
    (5,'Clothing or Footwear'),
    (6, 'Household shopping'),
    (7, 'Other- specify in remarks'),
    )
    category=models.IntegerField(choices=categories)
    remarks=models.CharField(max_length=264,null=True)
    def __str__(self):
        return self.T_id


class mandatory_expenses(models.Model):
    T_id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(User,  on_delete=models.CASCADE,)
    amount=models.IntegerField()
    categories=(
    (1,'Food'),
    (2,'Travel'),
    (3,'Groceries'),
    (4, 'Electronics'),
    (5,'Clothing or Footwear'),
    (6, 'Household shopping'),
    (7, 'Other- specify in remarks'),
    )
    category=models.IntegerField(choices=categories)
    remarks=models.CharField(max_length=264, null=True)
    def __str__(self):
        return self.T_id


class debts(models.Model):
    T_id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(User,  on_delete=models.CASCADE,)
    amount=models.IntegerField()
    reciever=models.CharField(max_length=264)
    remarks=models.CharField(max_length=264)
    Deadline=models.DateField()
    date_time=models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.T_id


# class notifications(models.Model):
#     N_id=models.AutoField(primary_key=True)
#     Email=models.ForeignKey
