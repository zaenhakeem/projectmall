# Generated by Django 4.0.3 on 2022-04-07 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_featuredproduct_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='hometown_admin', max_length=200)),
                ('email', models.CharField(default='admin', max_length=200)),
                ('message', models.CharField(default='admin', max_length=200)),
                ('subject', models.CharField(default='admin', max_length=200)),
            ],
        ),
    ]
