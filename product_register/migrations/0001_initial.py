# Generated by Django 3.2.6 on 2021-08-25 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product_option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_description', models.CharField(max_length=100)),
                ('product_price', models.CharField(max_length=100)),
                ('delivery_price', models.CharField(max_length=100)),
                ('product_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_register.product_option')),
            ],
        ),
    ]