# Generated by Django 4.1.5 on 2023-04-08 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Urun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=20)),
                ('resim', models.FileField(null=True, upload_to='urun/')),
                ('kategori', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='urunler.kategori')),
            ],
        ),
    ]
