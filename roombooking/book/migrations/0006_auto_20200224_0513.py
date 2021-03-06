# Generated by Django 2.2.7 on 2020-02-24 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20200223_0549'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='room',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.Room'),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='slot_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Time_slots'),
        ),
    ]
