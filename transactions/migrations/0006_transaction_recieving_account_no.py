# Generated by Django 5.0.6 on 2024-06-25 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0005_remove_transaction_recieving_account_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='recieving_account_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]