# Generated by Django 4.2.4 on 2024-03-25 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vechile', '0003_alter_make_created_at_alter_make_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vechile',
            name='price',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vechile',
            name='purchase_rate',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
