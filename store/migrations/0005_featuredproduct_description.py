# Generated by Django 4.0.3 on 2022-03-29 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuredproduct',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
