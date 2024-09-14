# Generated by Django 4.2.11 on 2024-09-14 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='tax_rate',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Tax rate at the time of the order', max_digits=5, null=True),
        ),
    ]
