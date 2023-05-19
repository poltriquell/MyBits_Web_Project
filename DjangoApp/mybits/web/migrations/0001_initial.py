# Generated by Django 4.2 on 2023-05-19 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id_client', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('DNI_NIE', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('card_number', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Localization',
            fields=[
                ('id_localization', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id_order', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.client')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('id_restaurant', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=50)),
                ('longitude', models.FloatField(max_length=50)),
                ('latitude', models.FloatField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id_reservation', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('people_num', models.IntegerField()),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.client')),
                ('id_restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('id_restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id_order', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('id_producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.product')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='id_restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.restaurant'),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id_menu', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('id_restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.restaurant')),
            ],
        ),
    ]
