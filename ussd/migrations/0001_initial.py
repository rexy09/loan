# Generated by Django 3.2.3 on 2021-11-02 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TumaPesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_mtumaji', models.CharField(max_length=13)),
                ('no_mpokeaji', models.CharField(max_length=13)),
                ('kiasi', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
                ('tofauti', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
                ('jumla', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
