# Generated by Django 4.2.2 on 2023-08-10 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vechile', '0002_vechile_created_at_vechile_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='make',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='make',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='vechile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='vechile',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
