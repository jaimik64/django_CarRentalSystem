# Generated by Django 4.1 on 2022-11-26 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_dealer_portal', '0003_alter_area_pincode'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicles',
            name='img',
            field=models.ImageField(default=' ', upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='area',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='cardealer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
