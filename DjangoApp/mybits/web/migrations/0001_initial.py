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
            name='Restaurant',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('id_restaurant', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=50)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id_reservation', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('people_num', models.IntegerField()),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Client')),
                ('id_restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id_order', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('total_price', models.FloatField()),
                ('description', models.CharField(max_length=50)),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Client')),
                ('id_restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id_menu', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('description', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('id_restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Restaurant')),
            ],
        ),
    ]
