# Generated by Django 4.2.4 on 2023-08-28 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hordak', '0039_alter_account_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transaction_key',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
