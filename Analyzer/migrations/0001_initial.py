# Generated by Django 2.1.5 on 2019-03-07 10:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='debts',
            fields=[
                ('T_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('reciever', models.CharField(max_length=264)),
                ('remarks', models.CharField(max_length=264)),
                ('Deadline', models.DateField()),
                ('date_time', models.DateTimeField(default=datetime.datetime.now)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='general_expenses',
            fields=[
                ('T_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('date_time', models.DateTimeField(default=datetime.datetime.now)),
                ('category', models.IntegerField(choices=[(1, 'Food'), (2, 'Travel'), (3, 'Groceries'), (4, 'Electronics'), (5, 'Clothing or Footwear'), (6, 'Household shopping'), (7, 'Other- specify in remarks')])),
                ('remarks', models.CharField(max_length=264, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='mandatory_expenses',
            fields=[
                ('T_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('category', models.IntegerField(choices=[(1, 'Food9'), (2, 'Travel'), (3, 'Groceries'), (4, 'Electronics'), (5, 'Clothing or Footwear'), (6, 'Household shopping'), (7, 'Other- specify in remarks')])),
                ('remarks', models.CharField(max_length=264, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='user_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PhoneNo', models.IntegerField(null=True)),
                ('Wallet', models.IntegerField(null=True)),
                ('frequent_wallet_addition_amount', models.IntegerField(null=True)),
                ('amount_to_be_added', models.IntegerField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
