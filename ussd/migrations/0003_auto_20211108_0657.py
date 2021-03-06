# Generated by Django 3.2.8 on 2021-11-08 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ussd', '0002_tumapesa1_tumapesa2_tumapesa3_tumapesa4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sajili',
            name='balance',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='tumapesa',
            name='jumla',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='tumapesa',
            name='kiasi',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='tumapesa',
            name='tofauti',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='tumapesa1',
            name='jumla',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='tumapesa1',
            name='kiasi',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='tumapesa1',
            name='tofauti',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='tumapesa2',
            name='jumla',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='tumapesa2',
            name='kiasi',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='tumapesa2',
            name='tofauti',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='tumapesa3',
            name='jumla',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='tumapesa3',
            name='kiasi',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='tumapesa3',
            name='tofauti',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='tumapesa4',
            name='jumla',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='tumapesa4',
            name='kiasi',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='tumapesa4',
            name='tofauti',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=19),
        ),
    ]
