# Generated by Django 2.0.5 on 2018-09-19 14:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('testcase', '0002_auto_20180914_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='last_edit_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='precondition',
            field=models.TextField(max_length=255, null=True),
        ),
    ]