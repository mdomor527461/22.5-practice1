# Generated by Django 5.0.6 on 2024-06-26 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0019_transaction_is_bankrupt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='is_bankrupt',
        ),
    ]