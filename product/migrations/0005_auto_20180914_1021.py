# Generated by Django 2.1.1 on 2018-09-14 02:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('product', '0004_auto_20180912_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]
