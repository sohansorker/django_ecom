# Generated by Django 3.1 on 2021-01-09 18:26

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_auto_20210109_1848'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='product',
            name='new_price_gt_0',
        ),
        migrations.RemoveConstraint(
            model_name='product',
            name='old_price_gt_0',
        ),
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
    ]
