# Generated by Django 3.2.3 on 2021-11-03 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ussd', '0003_auto_20211103_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tumapesa',
            name='tofauti',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=19),
        ),
    ]