# Generated by Django 4.1 on 2022-11-26 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_dealer_portal', '0004_vehicles_img_alter_area_id_alter_cardealer_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicles',
            name='dealer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_dealer_portal.cardealer'),
        ),
    ]
