# Generated by Django 3.2.6 on 2021-08-30 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_option',
        ),
        migrations.DeleteModel(
            name='product_option',
        ),
        migrations.AddField(
            model_name='productoption',
            name='Product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product_register.product'),
        ),
    ]
