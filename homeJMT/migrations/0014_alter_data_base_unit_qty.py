# Generated by Django 4.0.6 on 2022-07-22 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeJMT', '0013_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='Base_Unit_Qty',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
