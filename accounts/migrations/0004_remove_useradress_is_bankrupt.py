# Generated by Django 5.0.6 on 2024-06-26 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_useradress_is_bankrupt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useradress',
            name='is_bankrupt',
        ),
    ]
