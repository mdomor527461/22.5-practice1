# Generated by Django 5.0.6 on 2024-06-26 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0013_alter_transaction_balance_after_transaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='balance_after_transaction',
        ),
    ]
