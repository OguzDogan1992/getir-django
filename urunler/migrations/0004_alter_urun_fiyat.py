# Generated by Django 4.1.5 on 2023-04-08 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0003_urun_fiyat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urun',
            name='fiyat',
            field=models.FloatField(),
        ),
    ]