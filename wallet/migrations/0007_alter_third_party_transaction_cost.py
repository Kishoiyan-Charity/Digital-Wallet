# Generated by Django 4.0.6 on 2022-08-01 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0006_alter_loan_interest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='third_party',
            name='transaction_cost',
            field=models.IntegerField(),
        ),
    ]
