# Generated by Django 3.2.3 on 2021-11-02 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ussd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tumapesa',
            name='tofauti',
            field=models.IntegerField(),
        ),
    ]
