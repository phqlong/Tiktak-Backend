# Generated by Django 3.1.12 on 2021-08-23 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210824_0205'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='order',
            name='create_date',
        ),
        migrations.RemoveField(
            model_name='orderline',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='orderline',
            name='product_id',
        ),
        migrations.AddField(
            model_name='order',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='paymentMethod',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='shippingCost',
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='totalCost',
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='orderline',
            name='order',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.order'),
        ),
        migrations.AddField(
            model_name='orderline',
            name='product',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product'),
        ),
        migrations.AlterField(
            model_name='orderline',
            name='sub_total',
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('order', models.OneToOneField(blank=True, null=True,
                                               on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
        ),
    ]
