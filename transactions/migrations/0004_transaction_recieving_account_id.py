# Generated by Django 5.0.6 on 2024-06-24 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_rename_loan_aprove_transaction_loan_approve_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='recieving_account_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
